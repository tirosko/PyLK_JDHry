# 1) pygame.Rect(...) - Vytvorí štvorec, ktorý vie testovať kolízie.
# 2) event.type == pygame.MOUSEBUTTONDOWN - Zachytí kliknutie myši.
# 3) rect.collidepoint(event.pos) - Zistí, či súradnice kliknutia sú vo vnútri štvorca.

import pygame
pygame.init()

# Okno
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kliknutie na štvorec")

# Štvorec (Rect)
rect = pygame.Rect(200, 150, 150, 100)  # x, y, šírka, výška
rect_color = (0, 120, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detekcia kliknutia
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                print("Klikol si na štvorec")
                rect_color = (255, 80, 80)  # zmena farby po kliknutí
            else:
                print("Klikol si mimo štvorca")
                rect_color = (0, 120, 255)  # reset farby    

    # Kreslenie
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()

pygame.quit()
