#!/usr/bin/env python
"""Test program bez interaktívneho vstupu"""

import sys
sys.path.insert(0, r'.')

# Importujeme len classes a funkcie
import math

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("ERROR: Pygame nie je dostupný!")

class KockaVisualizer:
    """Vizualizácia kocky s farbami."""
    
    # Mapovanie farieb na RGB
    FARBY_RGB = {
        'R': (255, 0, 0),        # Červená
        'G': (0, 200, 0),        # Zelená
        'B': (0, 0, 255),        # Modrá
        'N': (200, 200, 200)     # Neutrálna (sivá)
    }
    
    # Vrcholy jednotkovej kocky
    VRCHOLY = [
        [-1, -1, -1],  # 0
        [1, -1, -1],   # 1
        [1, 1, -1],    # 2
        [-1, 1, -1],   # 3
        [-1, -1, 1],   # 4
        [1, -1, 1],    # 5
        [1, 1, 1],     # 6
        [-1, 1, 1],    # 7
    ]
    
    # Faces: indexy vrcholov každej steny
    # Poradie: top, bottom, front, back, left, right
    STENY = [
        [3, 2, 6, 7],    # Top (vrch) - index 0
        [0, 1, 5, 4],    # Bottom (spodok) - index 1
        [0, 1, 2, 3],    # Front (predok) - index 2
        [4, 5, 6, 7],    # Back (zámer) - index 3
        [0, 3, 7, 4],    # Left (vľavo) - index 4
        [1, 2, 6, 5],    # Right (vpravo) - index 5
    ]
    
    def __init__(self, stav_kocky):
        self.stav_kocky = stav_kocky
        self.rot_x = 0.5
        self.rot_y = 0.5
        self.rot_z = 0
        print(f"KockaVisualizer inicializovaná: {stav_kocky}")
        
    def rotuj_bod(self, bod, rx, ry, rz):
        """Rotuje bod v 3D priestore."""
        x, y, z = bod
        
        # Rotácia okolo X osi
        y_new = y * math.cos(rx) - z * math.sin(rx)
        z_new = y * math.sin(rx) + z * math.cos(rx)
        y, z = y_new, z_new
        
        # Rotácia okolo Y osi
        x_new = x * math.cos(ry) + z * math.sin(ry)
        z_new = -x * math.sin(ry) + z * math.cos(ry)
        x, z = x_new, z_new
        
        # Rotácia okolo Z osi
        x_new = x * math.cos(rz) - y * math.sin(rz)
        y_new = x * math.sin(rz) + y * math.cos(rz)
        x, y = x_new, y_new
        
        return [x, y, z]
    
    def projekt_3d_na_2d(self, bod, sirka, vyska):
        """Projektuje 3D bod na 2D obrazovku."""
        scale = 100
        x, y, z = bod
        
        # Perspektívna projekcia
        vzdalenost = 4 + z
        x2d = int(sirka/2 + (x / vzdalenost) * scale)
        y2d = int(vyska/2 - (y / vzdalenost) * scale)
        
        return (x2d, y2d, z)  # Vrátime z pre zoradenie
    
    def nakresli_pygame(self):
        """Interaktívna vizualizácia v Pygame."""
        if not PYGAME_AVAILABLE:
            print("Pygame nie je nainštalovaný!")
            return
        
        print("Spúšťam Pygame vizualizáciu...")
        pygame.init()
        sirka, vyska = 800, 600
        screen = pygame.display.set_mode((sirka, vyska))
        pygame.display.set_caption("Kocka s farbami")
        clock = pygame.time.Clock()
        
        font = pygame.font.Font(None, 24)
        
        frame_count = 0
        running = True
        while running:
            frame_count += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Automaticky rotujeme kocku
            self.rot_x += 0.005
            self.rot_y += 0.007
            
            # Transformácia a projekcia vrcholov
            vrcholy_3d = []
            vrcholy_2d = []
            for vrchol in self.VRCHOLY:
                rot = self.rotuj_bod(vrchol[:], self.rot_x, self.rot_y, self.rot_z)
                proj = self.projekt_3d_na_2d(rot, sirka, vyska)
                vrcholy_3d.append(rot)
                vrcholy_2d.append(proj)
            
            # Maľovanie
            screen.fill((50, 50, 50))
            
            # Zoraďovanie stien podľa z-koordináty (painter's algorithm)
            steny_sorted = []
            for idx, sten in enumerate(self.STENY):
                z_avg = sum(vrcholy_3d[v][2] for v in sten) / len(sten)
                steny_sorted.append((z_avg, idx, sten))
            
            steny_sorted.sort()
            
            # Počítač stien na kreslenie
            drawn_faces = 0
            
            # Maľovanie stien
            for z_avg, idx, sten in steny_sorted:
                farba = self.FARBY_RGB[self.stav_kocky[idx]]
                body = [tuple(vrcholy_2d[v][:2]) for v in sten]
                
                # Skontrolujeme, či máme aspoň 3 body pre kreslenie polygónu
                if len(body) >= 3:
                    try:
                        pygame.draw.polygon(screen, farba, body)
                        pygame.draw.polygon(screen, (0, 0, 0), body, 3)
                        drawn_faces += 1
                    except Exception as e:
                        print(f"Chyba pri kreslení steny {idx}: {e}")
            
            if frame_count % 60 == 0:
                print(f"Frame {frame_count}: nakreslené {drawn_faces} stien")
            
            # Text informácie
            text1 = font.render(f"Kocka: {self.stav_kocky}", True, (255, 255, 255))
            text2 = font.render("Stlač ESC na zatvorenie", True, (200, 200, 200))
            screen.blit(text1, (10, 10))
            screen.blit(text2, (10, vyska - 30))
            
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
        print(f"Pygame zatvorený, spustilo sa {frame_count} framov")

# Test
if __name__ == "__main__":
    print("Začínam test...")
    kocka = ('R', 'G', 'B', 'N', 'N', 'N')
    viz = KockaVisualizer(kocka)
    viz.nakresli_pygame()
