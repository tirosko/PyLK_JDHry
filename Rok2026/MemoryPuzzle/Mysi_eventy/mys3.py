# 1) offset_x / offset_y - Keď klikneš na štvorec, uloží sa rozdiel medzi pozíciou myši a pozíciou štvorca.
# Vďaka tomu sa štvorec nepreskočí pod kurzor, ale drží sa presne tam, kde si ho chytil.

# 2) dragging = True - Tento boolean signalizuje, že momentálne držíš štvorec a chceš ho presunúť. Keď je True, program ví, že má aktualizovat poziciu štvorca podle pohybu myši.
# Aktivuje režim ťahania.

# 3) MOUSEMOTION - Počas pohybu myši sa štvorec presúva podľa kurzora.

# 4) MOUSEBUTTONUP - Uvoľní objekt a vráti farbu.

import pygame
pygame.init()

# Okno
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag & Drop štvorec")

# Štvorec
rect = pygame.Rect(200, 150, 150, 100)
rect_color = (0, 120, 255)

dragging = False
offset_x = 0
offset_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Začiatok ťahania
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = rect.x - mouse_x
                offset_y = rect.y - mouse_y
                rect_color = (255, 80, 80)  # farba pri chytení

        # Pohyb počas ťahania
        if event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                rect.x = mouse_x + offset_x
                rect.y = mouse_y + offset_y

        # Koniec ťahania
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            rect_color = (0, 120, 255)

    # Kreslenie
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()

pygame.quit()
