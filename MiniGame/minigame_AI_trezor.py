import pygame
import random
import sys
import os

pygame.init()  # Init pygame
W, H = 600, 600  # Screen setup

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch the Falling Circles")

WHT, BLU, RED, BLK = (255, 255, 255), (0, 200,
                                       255), (255, 0, 0), (0, 0, 0)  # Colors

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Get script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
sound_folder = os.path.join(script_dir, 'Sounds')
# Load sounds
sound_path2 = os.path.join(sound_folder, 'match1.wav')
paddle_sound = pygame.mixer.Sound(sound_path2)

# Paddle
paddle = pygame.Rect(W // 2 - 56, H - 20, 113, 20)

# Circles list
circles = []
initial_speed = 5
spawn_timer = 0
spawn_interval = 60  # frames, about 1 second at 60 FPS

score = 0  # Score

# control flags
started = False  # wait for start command
sound_enabled = True  # sounds on/off

# Game loop
run = True
while run:
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # ctrl+s via event to reliably stop sound
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s and (e.mod & pygame.KMOD_CTRL):
            pygame.mixer.stop()
        # toggle sound on start screen
        if not started and e.type == pygame.KEYDOWN and e.key == pygame.K_m:
            sound_enabled = not sound_enabled

    keys = pygame.key.get_pressed()

    # start command: press SPACE to begin
    if not started:
        if keys[pygame.K_SPACE]:
            started = True
        else:
            # display prompt and sound option
            prompt = font.render("Press SPACE to start", True, WHT)
            status = "ON" if sound_enabled else "OFF"
            sound_text = font.render(f"Sound (M): {status}", True, WHT)
            screen.blit(prompt, (W//2 - 120, H//2 - 20))
            screen.blit(sound_text, (W//2 - 120, H//2 + 20))
            pygame.display.flip()
            clock.tick(60)
            continue

    # Paddle movement
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.move_ip(8, 0)

    # Spawn new circles
    spawn_timer += 1
    if spawn_timer >= spawn_interval:
        circles.append({
            'x': random.randint(10, W - 10),
            'y': 0,
            'radius': 10,
            'speed': initial_speed
        })
        spawn_timer = 0

    # Move circles
    for circle in circles[:]:
        circle['y'] += circle['speed']

    # Check collisions
    for circle in circles[:]:
        if circle['y'] + circle['radius'] >= paddle.top and paddle.left <= circle['x'] <= paddle.right:
            circles.remove(circle)
            if sound_enabled:
                paddle_sound.play()
            score += 1
            # Increase speed for all circles
            for c in circles:
                c['speed'] += 0.1
            initial_speed += 0.1

    # Remove missed circles
    for circle in circles[:]:
        if circle['y'] - circle['radius'] > H:
            circles.remove(circle)
            # Game over if any circle is missed
            game_over = font.render(
                f"Game Over! Final Score: {score}", True, RED)
            screen.blit(game_over, (W // 2 - 150, H // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            run = False
            break

    # Draw objects
    pygame.draw.rect(screen, WHT, paddle)
    for circle in circles:
        pygame.draw.circle(
            screen, RED, (circle['x'], circle['y']), circle['radius'])

    # Display score
    score_text = font.render(f"Score: {score}", True, WHT)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
