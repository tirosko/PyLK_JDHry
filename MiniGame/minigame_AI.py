import pygame
import random
import sys
import os

pygame.init()  # Init pygame
W, H = 600, 600  # Screen setup

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Catch the Falling Circles")

# colors
WHT = (255, 255, 255)
BLU = (0, 200, 255)
RED = (255, 0, 0)
BLK = (0, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# load sound
script_dir = os.path.dirname(os.path.abspath(__file__))
sound_folder = os.path.join(script_dir, 'Sounds')
sound_path = os.path.join(sound_folder, 'match1.wav')
paddle_sound = pygame.mixer.Sound(sound_path)

# paddle setup (113px wide, 20px high)
paddle = pygame.Rect(W // 2 - 113 // 2, H - 20, 113, 20)

# circle container
circles = []

b_speed = 5  # base falling speed

score = 0

def spawn_circle():
    x = random.randint(10, W - 10)
    return {'x': x, 'y': 0, 'r': 10, 'speed': b_speed}

# ensure at least one circle is active
if not circles:
    circles.append(spawn_circle())

run = True
while run:
    screen.fill(BLK)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-8, 0)
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.move_ip(8, 0)

    # update circles
    for circle in circles[:]:
        circle['y'] += circle['speed']

        # check catch
        if circle['y'] + circle['r'] >= paddle.top and paddle.left <= circle['x'] <= paddle.right:
            paddle_sound.play()
            score += 1
            b_speed += 0.5
            circles.remove(circle)

        # check miss
        elif circle['y'] - circle['r'] > H:
            game_over = font.render(f"Game Over! Final Score: {score}", True, RED)
            screen.blit(game_over, (W // 2 - 150, H // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            run = False
            break

    # spawn a new circle if none present
    if not circles and run:
        circles.append(spawn_circle())

    # draw
    pygame.draw.rect(screen, WHT, paddle)
    for circle in circles:
        pygame.draw.circle(screen, BLU, (int(circle['x']), int(circle['y'])), circle['r'])

    score_text = font.render(f"Score: {score}", True, WHT)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
