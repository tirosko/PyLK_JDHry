import pygame
pygame.init()

# Okno
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Viac objektov + Kolízie")

GRID = 20

def snap(value, grid):
    return round(value / grid) * grid

def draw_grid(surface, grid_size):
    color = (50, 50, 50)
    for x in range(0, WIDTH, grid_size):
        pygame.draw.line(surface, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_size):
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

# Objekty
objects = [
    pygame.Rect(50, 50, 120, 80),
    pygame.Rect(250, 80, 150, 100),
    pygame.Rect(150, 200, 100, 120)
]

colors = [
    (0, 120, 255),
    (0, 200, 120),
    (200, 120, 0)
]

dragging = False
selected = None
offset_x = 0
offset_y = 0

def collides_with_others(rect, index):
    """Vráti True, ak rect koliduje s iným objektom."""
    for i, other in enumerate(objects):
        if i != index and rect.colliderect(other):
            return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Výber objektu
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in reversed(range(len(objects))):
                if objects[i].collidepoint(event.pos):
                    selected = i
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = objects[i].x - mouse_x
                    offset_y = objects[i].y - mouse_y
                    colors[i] = (255, 80, 80)
                    break

        # Pohyb + kolízie
        if event.type == pygame.MOUSEMOTION and dragging and selected is not None:
            mouse_x, mouse_y = event.pos
            obj = objects[selected]

            old_x, old_y = obj.x, obj.y  # uložíme pôvodnú pozíciu

            obj.x = mouse_x + offset_x
            obj.y = mouse_y + offset_y

            # Obmedzenie na okno
            if obj.x < 0:
                obj.x = 0
            if obj.y < 0:
                obj.y = 0
            if obj.right > WIDTH:
                obj.right = WIDTH
            if obj.bottom > HEIGHT:
                obj.bottom = HEIGHT

            # Kolízia → vrátime pôvodnú pozíciu
            if collides_with_others(obj, selected):
                obj.x, obj.y = old_x, old_y

        # Pustenie + snap
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging and selected is not None:
                obj = objects[selected]

                old_x, old_y = obj.x, obj.y
                obj.x = snap(obj.x, GRID)
                obj.y = snap(obj.y, GRID)

                # Ak snap spôsobí kolíziu, vrátime späť
                if collides_with_others(obj, selected):
                    obj.x, obj.y = old_x, old_y

                colors[selected] = (0, 120, 255)

            dragging = False
            selected = None

    # Kreslenie
    screen.fill((30, 30, 30))
    draw_grid(screen, GRID)

    for i, rect in enumerate(objects):
        pygame.draw.rect(screen, colors[i], rect)

    pygame.display.flip()

pygame.quit()
