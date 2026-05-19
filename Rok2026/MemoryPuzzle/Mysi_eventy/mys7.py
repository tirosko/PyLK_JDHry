# Ako to funguje
# ✔ 1. Viac objektov - Používame zoznam objects = [Rect, Rect, Rect].

# ✔ 2. Výber objektu podľa poradia (zvrchu) - Prechádzame objekty odzadu, aby sa vybral ten, ktorý je „navrchu“.

# ✔ 3. Každý objekt má vlastnú farbu
# Farba sa zmení pri chytení a vráti späť po pustení.

# ✔ 4. Drag & Drop
# Presne ako predtým, ale teraz pre konkrétny objekt.

# ✔ 5. Obmedzenie pohybu
# Objekt nikdy nevyjde mimo okno.

# ✔ 6. Magnetické pripínanie
# Po pustení sa objekt pripne na najbližší grid bod.

# ✔ 7. Vizuálna mriežka
# Automaticky sa prispôsobí veľkosti GRID.


import pygame
pygame.init()

# Okno
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Viac objektov + Drag & Drop + Grid Snap")

# Mriežka
GRID = 20

def snap(value, grid):
    return round(value / grid) * grid

def draw_grid(surface, grid_size):
    color = (50, 50, 50)
    for x in range(0, WIDTH, grid_size):
        pygame.draw.line(surface, color, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, grid_size):
        pygame.draw.line(surface, color, (0, y), (WIDTH, y))

# Viac objektov
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Kliknutie – vyber objekt
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in reversed(range(len(objects))):  # kontrola zhora
                if objects[i].collidepoint(event.pos):
                    selected = i
                    dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = objects[i].x - mouse_x
                    offset_y = objects[i].y - mouse_y
                    colors[i] = (255, 80, 80)  # zvýraznenie
                    break

        # Pohyb myši počas ťahania
        if event.type == pygame.MOUSEMOTION and dragging and selected is not None:
            mouse_x, mouse_y = event.pos
            obj = objects[selected]

            obj.x = mouse_x + offset_x
            obj.y = mouse_y + offset_y

            # Obmedzenie pohybu na okno
            if obj.x < 0:
                obj.x = 0
            if obj.y < 0:
                obj.y = 0
            if obj.right > WIDTH:
                obj.right = WIDTH
            if obj.bottom > HEIGHT:
                obj.bottom = HEIGHT

        # Pustenie – snap na mriežku
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging and selected is not None:
                obj = objects[selected]
                obj.x = snap(obj.x, GRID)
                obj.y = snap(obj.y, GRID)
                colors[selected] = (0, 120, 255)  # späť na farbu
            dragging = False
            selected = None

    # Kreslenie
    screen.fill((30, 30, 30))
    draw_grid(screen, GRID)

    for i, rect in enumerate(objects):
        pygame.draw.rect(screen, colors[i], rect)

    pygame.display.flip()

pygame.quit()
