import pygame
pygame.init()

# Okno
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drag & Drop + Grid Snap + Mriežka")

# Štvorec
rect = pygame.Rect(200, 150, 150, 100)
rect_color = (0, 120, 255)

dragging = False
offset_x = 0
offset_y = 0

GRID = 20  # veľkosť mriežky

def snap(value, grid):
    return round(value / grid) * grid

def draw_grid(surface, grid_size):
    color = (50, 50, 50)
    # Vertikálne čiary
    for x in range(0, WIDTH, grid_size):
        pygame.draw.line(surface, color, (x, 0), (x, HEIGHT))
    # Horizontálne čiary
    for y in range(0, HEIGHT, grid_size):
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

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
                rect_color = (255, 80, 80)

        # Pohyb počas ťahania
        if event.type == pygame.MOUSEMOTION and dragging:
            mouse_x, mouse_y = event.pos
            rect.x = mouse_x + offset_x
            rect.y = mouse_y + offset_y

            # Obmedzenie pohybu na okno
            if rect.x < 0:
                rect.x = 0
            if rect.y < 0:
                rect.y = 0
            if rect.right > WIDTH:
                rect.right = WIDTH
            if rect.bottom > HEIGHT:
                rect.bottom = HEIGHT

        # Koniec ťahania + pripnutie na mriežku
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                rect.x = snap(rect.x, GRID)
                rect.y = snap(rect.y, GRID)
            dragging = False
            rect_color = (0, 120, 255)

    # Kreslenie
    screen.fill((30, 30, 30))
    draw_grid(screen, GRID)
    pygame.draw.rect(screen, rect_color, rect)
    pygame.display.flip()

pygame.quit()
