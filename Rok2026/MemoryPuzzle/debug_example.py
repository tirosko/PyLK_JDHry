import pygame
import logging

# -----------------------------
# Logging (zapni/vypni podľa potreby)
# -----------------------------
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

# -----------------------------
# Inicializácia
# -----------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Debug Template")

clock = pygame.time.Clock()
running = True

# -----------------------------
# Príklad hráča
# -----------------------------
player = pygame.Rect(100, 100, 50, 50)
player_speed = 5

# -----------------------------
# Debug nastavenia
# -----------------------------
SHOW_HITBOXES = True
SHOW_FPS = True
FONT = pygame.font.SysFont("consolas", 20)


def draw_debug_overlay():
    """Vykreslí FPS a ďalšie debug info."""
    if SHOW_FPS:
        fps_text = FONT.render(
            f"FPS: {clock.get_fps():.1f}", True, (255, 255, 0))
        screen.blit(fps_text, (10, 10))

    pos_text = FONT.render(
        f"Player: {player.x}, {player.y}", True, (0, 255, 255))
    screen.blit(pos_text, (10, 35))


def draw_hitboxes():
    """Vykreslí hitboxy objektov."""
    pygame.draw.rect(screen, (255, 0, 0), player, 2)


# -----------------------------
# Hlavná herná slučka
# -----------------------------
while running:
    clock.tick(60)  # limit FPS

    # -------------------------
    # Event loop
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Debug: logovanie stlačených kláves
        if event.type == pygame.KEYDOWN:
            logging.debug(f"Key pressed: {pygame.key.name(event.key)}")

    # -------------------------
    # Input
    # -------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # -------------------------
    # Render
    # -------------------------
    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 150, 255), player)

    if SHOW_HITBOXES:
        draw_hitboxes()

    draw_debug_overlay()

    pygame.display.flip()

pygame.quit()
