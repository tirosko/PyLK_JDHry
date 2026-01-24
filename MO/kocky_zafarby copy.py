"""
Problém: Václav mal kocky s 3 zafarbený stenami (červená, zelená, modrá).
Koľko rôznych typov kociek mohol vytvoriť, ak dva typy sú rovnaké,
keď sa dá jedna kocka otočiť tak, aby vyzerala ako druhá?

Riešenie: Predstavujeme kocku ako pole 6 stien. Generujeme všetky možné
zafarbenia, potom ich rozdelíme do tried podľa rotácií kocky.
"""

from itertools import combinations, permutations
import math
import random

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False


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
        """
        Args:
            stav_kocky: tuple s 6 farbami stien (v poradí: top, bottom, front, back, left, right)
        """
        self.stav_kocky = stav_kocky
        self.rot_x = 0.5
        self.rot_y = 0.5
        self.rot_z = 0
        
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
        
        return [x2d, y2d, z]
    
    def nakresli_ascii(self):
        """Jednoduchá ASCII reprezentácia kocky."""
        print("\n    Vizualizácia kocky (ASCII):")
        print("    " + "=" * 16)
        print(f"    Top:    [{self.stav_kocky[0]}]")
        print(f"    Bottom: [{self.stav_kocky[1]}]")
        print(f"    Front:  [{self.stav_kocky[2]}]")
        print(f"    Back:   [{self.stav_kocky[3]}]")
        print(f"    Left:   [{self.stav_kocky[4]}]")
        print(f"    Right:  [{self.stav_kocky[5]}]")
        print("    " + "=" * 16)
    
    def nakresli_pygame(self):
        """Interaktívna vizualizácia v Pygame."""
        if not PYGAME_AVAILABLE:
            print("Pygame nie je nainštalovaný. Inštalácia: pip install pygame")
            return
        
        pygame.init()
        sirka, vyska = 800, 600
        screen = pygame.display.set_mode((sirka, vyska))
        pygame.display.set_caption("Kocka s farbami")
        clock = pygame.time.Clock()
        
        font = pygame.font.Font(None, 24)
        
        running = True
        while running:
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
            vrcholy_2d = []
            for vrchol in self.VRCHOLY:
                rot = self.rotuj_bod(vrchol, self.rot_x, self.rot_y, self.rot_z)
                proj = self.projekt_3d_na_2d(rot, sirka, vyska)
                vrcholy_2d.append(proj)
            
            # Maľovanie
            screen.fill((50, 50, 50))
            
            # Zoraďovanie stien podľa z-koordináty (painter's algorithm)
            steny_sorted = []
            for idx, sten in enumerate(self.STENY):
                z_avg = sum(vrcholy_2d[v][2] for v in sten) / len(sten)
                steny_sorted.append((z_avg, idx, sten))
            
            steny_sorted.sort()
            
            # Maľovanie stien
            for z_avg, idx, sten in steny_sorted:
                farba = self.FARBY_RGB[self.stav_kocky[idx]]
                body = [tuple(vrcholy_2d[v][:2]) for v in sten]
                pygame.draw.polygon(screen, farba, body)
                pygame.draw.polygon(screen, (0, 0, 0), body, 3)
            
            # Text informácie
            text1 = font.render(f"Kocka: {self.stav_kocky}", True, (255, 255, 255))
            text2 = font.render("Stlač ESC na zatvorenie", True, (200, 200, 200))
            screen.blit(text1, (10, 10))
            screen.blit(text2, (10, vyska - 30))
            
            pygame.display.flip()
            clock.tick(60)
        
        pygame.quit()
    
    def nakresli(self):
        """Vyberie vhodný spôsob vizualizácie."""
        if PYGAME_AVAILABLE:
            try:
                self.nakresli_pygame()
            except Exception as e:
                print(f"Chyba pri Pygame vizualizácii: {e}")
                self.nakresli_ascii()
        else:
            self.nakresli_ascii()


class Kocka:
    """Reprezentácia zafarbenej kocky."""
    
    # Indexy stien: 0=vrch, 1=spodok, 2=predok, 3=zámer, 4=vľavo, 5=vpravo
    # Všetky 24 rotácií kocky (permutácie stien)
    ROTACIE = [
        # Identita a otáčanie okolo osi Z (vrch-spodok)
        (0, 1, 2, 3, 4, 5),  # identita
        (0, 1, 3, 4, 2, 5),  # 90° okolo Z
        (0, 1, 3, 2, 4, 5),  # 180° okolo Z
        (0, 1, 4, 3, 2, 5),  # 270° okolo Z
        
        # Otáčanie okolo osi X (vľavo-vpravo)
        (2, 3, 1, 0, 4, 5),  # 90° okolo X
        (1, 0, 3, 2, 4, 5),  # 180° okolo X
        (3, 2, 0, 1, 4, 5),  # 270° okolo X
        
        # Otáčanie okolo osi Y (predok-zámer)
        (4, 5, 2, 3, 1, 0),  # 90° okolo Y
        (1, 0, 2, 3, 5, 4),  # 180° okolo Y
        (5, 4, 2, 3, 0, 1),  # 270° okolo Y
        
        # Kombinované rotácie
        (2, 3, 5, 4, 0, 1),
        (2, 3, 0, 1, 5, 4),
        (3, 2, 4, 5, 1, 0),
        (3, 2, 1, 0, 5, 4),
        (4, 5, 0, 1, 3, 2),
        (4, 5, 3, 2, 1, 0),
        (5, 4, 1, 0, 3, 2),
        (5, 4, 3, 2, 0, 1),
        (0, 1, 5, 4, 3, 2),
        (2, 3, 4, 5, 0, 1),
        (1, 0, 4, 5, 2, 3),
        (3, 2, 5, 4, 1, 0),
        (4, 5, 2, 3, 0, 1),
        (5, 4, 2, 3, 1, 0),
    ]
    
    @staticmethod
    def je_validna_rotacia(perm):
        """Skontroluje, či je permutácia validnou rotáciou kocky."""
        # Jednoduchá kontrola - validná rotácia by mala zachovať štruktúru
        return len(perm) == 6 and len(set(perm)) == 6
    
    @staticmethod
    def rotuj(stav_kocky, rotacia_idx):
        """Aplikuje rotáciu na stav kocky.
        
        Args:
            stav_kocky: tuple 6 prvkov reprezentujúcich farby stien
            rotacia_idx: index rotácie
            
        Returns:
            Nový stav kocky po rotácii
        """
        rotacia = Kocka.ROTACIE[rotacia_idx]
        return tuple(stav_kocky[rotacia[i]] for i in range(6))
    
    @staticmethod
    def vsetky_rotacie(stav_kocky):
        """Vráti všetky rotácie daného stavu kocky."""
        rotacie = set()
        for i in range(len(Kocka.ROTACIE)):
            rotacia = Kocka.rotuj(stav_kocky, i)
            rotacie.add(rotacia)
        return rotacie
    
    @staticmethod
    def kanonicky_tvar(stav_kocky):
        """Vráti lexikograficky najmenšiu rotáciu (reprezentanta triedy)."""
        rotacie = Kocka.vsetky_rotacie(stav_kocky)
        return min(rotacie)


def generuj_vsetky_zafarby():
    """Generuje všetky možné zafarbenia kocky.
    
    - Vyberieme 3 steny z 6 na zafarbenie
    - Priradíme im farby R (červená), G (zelená), B (modrá)
    - Zvyšné 3 steny zostanú "N" (nezafarbené)
    
    Returns:
        Zoznam všetkých možných stavov kocky
    """
    zafarby = []
    farby = ['R', 'G', 'B']  # Červená, zelená, modrá
    
    # Vyberieme 3 steny z 6 na zafarbenie
    for farbene_steny in combinations(range(6), 3):
        # Pre vybrané steny generujeme všetky permutácie farieb
        for permutacia_farieb in permutations(farby):
            # Vytvoríme stav kocky
            stav = ['N'] * 6  # N = nezafarbená
            for i, sten_idx in enumerate(farbene_steny):
                stav[sten_idx] = permutacia_farieb[i]
            zafarby.append(tuple(stav))
    
    return zafarby


def pocet_skupin():
    """Spočíta počet různych typov kociek podľa rotácií."""
    vsetky_zafarby = generuj_vsetky_zafarby()
    print(f"Celkový počet možných zafarbení: {len(vsetky_zafarby)}")
    
    # Rozdelíme do tried ekvivalencie
    tripendency = {}
    kanonicky_tvary = set()
    
    for zafarby in vsetky_zafarby:
        kanon = Kocka.kanonicky_tvar(zafarby)
        kanonicky_tvary.add(kanon)
        
        if kanon not in tripendency:
            tripendency[kanon] = []
        tripendency[kanon].append(zafarby)
    
    # Výpis niektorých skupín
    print(f"\nPočet rôznych skupín: {len(kanonicky_tvary)}\n")
    
    # Ukážeme ako vyzerajú niektoré skupiny
    print("Príklady ekvivalenčných tried:")
    for i, (kanon, prvky) in enumerate(list(tripendency.items())[:5]):
        print(f"\nSkupina {i+1} (reprezentant: {kanon}):")
        print(f"  Počet prvkov: {len(prvky)}")
        if len(prvky) <= 3:
            for prvok in prvky:
                print(f"    - {prvok}")
        else:
            print(f"    - {prvky[0]}")
            print(f"    - {prvky[1]}")
            print(f"    ... ešte {len(prvky)-2}")
    
    return len(kanonicky_tvary)


if __name__ == "__main__":
    print("=" * 60)
    print("PROBLÉM: Koľko rôznych typov zafarbených kociek?")
    print("=" * 60)
    print("\nPopis:")
    print("- Kocka má 6 stien")
    print("- 3 steny sú zafarbené: červená (R), zelená (G), modrá (B)")
    print("- 3 steny sú nezafarbené (N)")
    print("- Dva typy kociek sú rovnaké, ak sa dá jedna otočiť na druh.")
    print("\n" + "=" * 60)
    
    odpoved = pocet_skupin()
    
    print("\n" + "=" * 60)
    print(f"ODPOVEĎ: Václav mohol vytvoriť {odpoved} RÔZNYCH SKUPÍN")
    print("=" * 60)
    
    # Vizualizácia niektorých kociek
    print("\n" + "=" * 60)
    print("VIZUALIZÁCIA KOCIEK")
    print("=" * 60)
    
    # Generujeme random zafarbené kocky a zobrazíme ich
    vsetky_zafarby = generuj_vsetky_zafarby()
    kanonicky_tvary = set()
    
    for zafarby in vsetky_zafarby:
        kanon = Kocka.kanonicky_tvar(zafarby)
        kanonicky_tvary.add(kanon)
    
    # Zobrazíme pár rôznych typov kociek
    kocky_na_zobrazenie = list(kanonicky_tvary)[:3]
    
    for i, kocka in enumerate(kocky_na_zobrazenie):
        print(f"\nKocka {i+1}: {kocka}")
        visualizer = KockaVisualizer(kocka)
        visualizer.nakresli_ascii()
    
    # Ponúkame interaktívnu vizualizáciu
    print("\n" + "=" * 60)
    if PYGAME_AVAILABLE:
        response = input("Chceš vidieť interaktívnu 3D vizualizáciu? (a/n): ").strip().lower()
        if response == 'a':
            # Vyberieme random kocku
            random_kocka = random.choice(list(kanonicky_tvary))
            print(f"\nZobrazujem kocku: {random_kocka}")
            visualizer = KockaVisualizer(random_kocka)
            visualizer.nakresli_pygame()
    else:
        print("Pre interaktívnu vizualizáciu nainštaluj Pygame: pip install pygame")
