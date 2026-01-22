"""Brick Blast - a simple Brick Breaker game using pygame.

Run: python -m BrickBlast.brick_blast
Requires: pygame (see requirements.txt)
"""
import sys
import random
import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
GREEN = (50, 180, 50)
BLUE = (50, 120, 200)
YELLOW = (230, 200, 50)


class Paddle(pygame.Rect):
    def __init__(self, x, y, w=100, h=16):
        super().__init__(x - w // 2, y - h // 2, w, h)
        self.speed = 8

    def move_left(self):
        self.x -= self.speed
        if self.left < 0:
            self.left = 0

    def move_right(self):
        self.x += self.speed
        if self.right > WIDTH:
            self.right = WIDTH


class Ball:
    def __init__(self, x, y, r=8):
        self.x = x
        self.y = y
        self.r = r
        self.speed = 6
        angle = random.uniform(-0.6, 0.6)
        self.vx = self.speed * angle
        self.vy = -self.speed * (1 - abs(angle))

    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r * 2, self.r * 2)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.r <= 0:
            self.x = self.r
            self.vx = -self.vx
        if self.x + self.r >= WIDTH:
            self.x = WIDTH - self.r
            self.vx = -self.vx
        if self.y - self.r <= 0:
            self.y = self.r
            self.vy = -self.vy


class Brick(pygame.Rect):
    def __init__(self, x, y, w, h, color, hits=1):
        super().__init__(x, y, w, h)
        self.color = color
        self.hits = hits


def make_bricks(rows=5, cols=10, top=60, padding=5):
    bricks = []
    brick_w = (WIDTH - (cols + 1) * padding) // cols
    brick_h = 28
    colors = [RED, ORANGE := (255,140,0), YELLOW, GREEN, BLUE]
    for row in range(rows):
        for col in range(cols):
            x = padding + col * (brick_w + padding)
            y = top + row * (brick_h + padding)
            color = colors[row % len(colors)]
            hits = 1 + (row // 3)
            bricks.append(Brick(x, y, brick_w, brick_h, color, hits))
    return bricks


def draw_text(surf, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    rect = img.get_rect()
    rect.topleft = (x, y)
    surf.blit(img, rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Brick Blast')
    clock = pygame.time.Clock()

    paddle = Paddle(WIDTH // 2, HEIGHT - 40)
    ball = Ball(WIDTH // 2, HEIGHT - 60)
    bricks = make_bricks()
    score = 0
    lives = 3
    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p:
                    paused = not paused
                if event.key == pygame.K_r:
                    # restart
                    paddle = Paddle(WIDTH // 2, HEIGHT - 40)
                    ball = Ball(WIDTH // 2, HEIGHT - 60)
                    bricks = make_bricks()
                    score = 0
                    lives = 3
                    paused = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle.move_right()

        if not paused:
            ball.update()

            # Ball misses bottom
            if ball.y - ball.r > HEIGHT:
                lives -= 1
                if lives <= 0:
                    # Game over
                    paused = True
                else:
                    ball = Ball(WIDTH // 2, HEIGHT - 60)

            # Paddle collision
            if ball.rect().colliderect(paddle):
                # reflect relative to where it hits the paddle
                offset = (ball.x - paddle.centerx) / (paddle.width / 2)
                ball.vx = ball.speed * offset
                ball.vy = -abs(ball.vy)

            # Brick collisions
            hit_index = None
            for i, b in enumerate(bricks):
                if ball.rect().colliderect(b):
                    hit_index = i
                    # Determine collision side
                    # Simple approach: reverse y velocity
                    ball.vy = -ball.vy
                    b.hits -= 1
                    if b.hits <= 0:
                        score += 10
                        bricks.pop(i)
                    else:
                        score += 5
                    break

            # Win condition - next level
            if not bricks:
                bricks = make_bricks(rows=6, cols=11, top=40)
                ball = Ball(WIDTH // 2, HEIGHT - 60)
                paddle = Paddle(WIDTH // 2, HEIGHT - 40)

        # Draw
        screen.fill(BLACK)

        for b in bricks:
            pygame.draw.rect(screen, b.color, b)
            pygame.draw.rect(screen, BLACK, b, 2)

        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.circle(screen, WHITE, (int(ball.x), int(ball.y)), ball.r)

        draw_text(screen, f'Score: {score}', 28, 8, 8)
        draw_text(screen, f'Lives: {lives}', 28, WIDTH - 120, 8)
        if paused:
            draw_text(screen, 'PAUSED - Press P to resume, R to restart', 30, WIDTH // 2 - 260, HEIGHT // 2 - 15, YELLOW)
            if lives <= 0:
                draw_text(screen, 'GAME OVER - Press R to restart', 36, WIDTH // 2 - 200, HEIGHT // 2 + 30, RED)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
