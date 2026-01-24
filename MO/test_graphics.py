"""Test graphics output"""
# import sys
import math

# Test basic math functions
bod = [-1, -1, -1]
rx, ry, rz = 0.5, 0.5, 0

# Rotácia okolo X osi
x, y, z = bod
y_new = y * math.cos(rx) - z * math.sin(rx)
z_new = y * math.sin(rx) + z * math.cos(rx)
y, z = y_new, z_new

print(f"Po rotácii: x={x}, y={y}, z={z}")

# Projekcia
scale = 100
sirka, vyska = 800, 600
vzdalenost = 4 + z
x2d = int(sirka/2 + (x / vzdalenost) * scale)
y2d = int(vyska/2 - (y / vzdalenost) * scale)

print(f"Projekcia: x2d={x2d}, y2d={y2d}")

# Test pygame
try:
    import pygame
    pygame.init()
    
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Test")
    
    screen.fill((50, 50, 50))
    
    # Nakreslíme bod/kruh
    pygame.draw.circle(screen, (255, 0, 0), (200, 150), 10)
    
    # Nakreslíme polygon (trojuholník)
    body = [(100, 100), (300, 100), (200, 250)]
    pygame.draw.polygon(screen, (0, 255, 0), body)
    pygame.draw.polygon(screen, (0, 0, 0), body, 3)
    
    pygame.display.flip()
    
    # Počkaj 2 sekundy
    pygame.time.wait(2000)
    
    pygame.quit()
    print("Pygame test OK - zobrazilo sa okno s grafickým prvkami")
    
except Exception as e:
    print(f"Chyba: {e}")
    import traceback
    traceback.print_exc()
