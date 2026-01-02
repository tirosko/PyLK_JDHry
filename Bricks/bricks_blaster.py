import pygame
import random
import sys

# Simple Bricks Blaster game
# - Bricks have integer values shown on them
# - Hitting a brick reduces its value; destroying a brick can spawn an extra ball
# Run: python -m Bricks.bricks_blaster  (or python Bricks/bricks_blaster.py)

WIDTH, HEIGHT = 800, 600
FPS = 60

BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30

MAX_BALLS = 6

pygame.init()
font = pygame.font.SysFont(None, 24)


class Brick:
    def __init__(self, x, y, value):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        self.value = value

    def color(self):
        # color mapping by value
        colors = {
            1: (200, 120, 120),
            2: (200, 180, 120),
            3: (160, 200, 120),
            4: (120, 180, 200),
            5: (180, 140, 220),
        }
        return colors.get(self.value, (200, 200, 200))

    def draw(self, surf):
        pygame.draw.rect(surf, self.color(), self.rect)
        txt = font.render(str(self.value), True, (10, 10, 10))
        tx = self.rect.centerx - txt.get_width() // 2
        ty = self.rect.centery - txt.get_height() // 2
        surf.blit(txt, (tx, ty))


class Ball:
    def __init__(self, x, y, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = 6
        self.trail = []

    def rect(self):
        return pygame.Rect(int(self.x - self.r), int(self.y - self.r), self.r*2, self.r*2)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        # record trail
        self.trail.append((self.x, self.y))
        if len(self.trail) > 12:
            self.trail.pop(0)

    def draw(self, surf):
        # draw trailing points
        tlen = len(self.trail)
        for i, (tx, ty) in enumerate(self.trail):
            alpha = int(80 * (i+1) / max(1, tlen))
            color = (150 + alpha, 150 + alpha, 255)
            pygame.draw.circle(surf, color, (int(tx), int(ty)), max(
                1, int(self.r * i / max(1, tlen))))

        pygame.draw.circle(surf, (250, 250, 250),
                           (int(self.x), int(self.y)), self.r)

        # draw simple projected trajectory line
        speed = (self.vx**2 + self.vy**2) ** 0.5
        if speed > 20:
            nx = self.vx / speed
            ny = self.vy / speed
            proj_len = 240
            endx = self.x + nx * proj_len
            endy = self.y + ny * proj_len
            pygame.draw.aaline(surf, (120, 160, 255), (int(
                self.x), int(self.y)), (int(endx), int(endy)))


class Paddle:
    def __init__(self):
        self.w = 100
        self.h = 12
        self.x = WIDTH // 2 - self.w // 2
        self.y = HEIGHT - 40
        self.speed = 500

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def draw(self, surf):
        pygame.draw.rect(surf, (220, 220, 220), self.rect())


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Bricks Blaster')
        self.clock = pygame.time.Clock()
        self.paddle = Paddle()
        self.balls = []
        self.attached = True
        self.lives = 3
        self.score = 0
        self.level = 1
        self.bricks = []
        self.spawn_level()
        self.reset_ball()

    def spawn_level(self):
        self.bricks.clear()
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                # randomize presence to create empty spaces
                chance = max(0.35, 0.8 - row * 0.08)
                if random.random() > chance:
                    continue
                x = col * BRICK_WIDTH + 1
                y = 40 + row * BRICK_HEIGHT
                # value depends on row (higher rows stronger)
                value = 1 + (BRICK_ROWS - row) // 2
                self.bricks.append(Brick(x, y, value))
        # ensure at least one brick exists
        if not self.bricks:
            col = random.randrange(BRICK_COLS)
            row = 0
            x = col * BRICK_WIDTH + 1
            y = 40 + row * BRICK_HEIGHT
            self.bricks.append(Brick(x, y, 1))

    def reset_ball(self, count=1):
        # attach `count` balls to paddle (centered/spread)
        self.balls = []
        base_x = self.paddle.x + self.paddle.w // 2
        spacing = 14
        if count <= 1:
            positions = [base_x]
        else:
            positions = [base_x + (i - (count-1)/2) *
                         spacing for i in range(count)]
        for px in positions:
            b = Ball(px, self.paddle.y - 10, 0, 0)
            self.balls.append(b)
        self.attached = True

    def launch_ball(self):
        if not self.balls:
            self.reset_ball()
        if self.attached:
            for b in self.balls:
                b.vx = random.uniform(-200, 200)
                b.vy = -350
            self.attached = False

    def spawn_extra_ball(self):
        if len(self.balls) >= MAX_BALLS:
            return
        x = self.paddle.x + self.paddle.w//2
        y = self.paddle.y - 10
        b = Ball(x, y, random.uniform(-200, 200), -300)
        self.balls.append(b)

    def handle_collisions(self, ball, dt):
        # walls
        if ball.x - ball.r <= 0:
            ball.x = ball.r
            ball.vx *= -1
        if ball.x + ball.r >= WIDTH:
            ball.x = WIDTH - ball.r
            ball.vx *= -1
        if ball.y - ball.r <= 0:
            ball.y = ball.r
            ball.vy *= -1

        # paddle
        if ball.rect().colliderect(self.paddle.rect()) and ball.vy > 0:
            offset = (ball.x - (self.paddle.x + self.paddle.w/2)) / \
                (self.paddle.w/2)
            ball.vx = offset * 400
            ball.vy *= -1
            ball.y = self.paddle.y - ball.r - 1

        # bricks
        for brick in self.bricks[:]:
            if ball.rect().colliderect(brick.rect):
                # simple bounce: reverse vy
                ball.vy *= -1
                brick.value -= 1
                if brick.value <= 0:
                    self.bricks.remove(brick)
                    self.score += 10
                    # spawn extra ball when a brick is destroyed
                    self.spawn_extra_ball()
                else:
                    self.score += 2
                break

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.x -= self.paddle.speed * dt
        if keys[pygame.K_RIGHT]:
            self.paddle.x += self.paddle.speed * dt
        self.paddle.x = max(0, min(WIDTH - self.paddle.w, self.paddle.x))

        # attached ball follows paddle
        if self.attached:
            for b in self.balls:
                b.x = self.paddle.x + self.paddle.w//2
                b.y = self.paddle.y - 10

        for b in self.balls[:]:
            if not self.attached:
                b.update(dt)
                self.handle_collisions(b, dt)
            # ball lost
            if b.y - b.r > HEIGHT:
                try:
                    self.balls.remove(b)
                except ValueError:
                    pass

        if not self.balls:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()
            else:
                self.reset_ball()

        if not self.bricks:
            # next level
            self.level += 1
            self.spawn_level()
            # start with 2 balls from level 2 onwards
            start_count = 2 if self.level >= 2 else 1
            self.reset_ball(count=start_count)
            # give bonus free balls when level is cleared (up to MAX_BALLS)
            bonus = min(2, MAX_BALLS - len(self.balls))
            for _ in range(bonus):
                bx = self.paddle.x + self.paddle.w // 2 + \
                    random.uniform(-20, 20)
                by = self.paddle.y - 10
                b = Ball(bx, by, random.uniform(-220, 220), -320)
                self.balls.append(b)

    def draw_hud(self):
        s = font.render(
            f'Score: {self.score}  Lives: {self.lives}  Balls: {len(self.balls)}', True, (240, 240, 240))
        self.screen.blit(s, (10, 10))

    def game_over(self):
        over = True
        while over:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_r:
                        self.__init__()
                        return
            self.screen.fill((10, 10, 30))
            txt = pygame.font.SysFont(None, 60).render(
                'Game Over', True, (240, 80, 80))
            self.screen.blit(
                txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2 - 40))
            txt2 = font.render(
                'Press R to restart or close window', True, (200, 200, 200))
            self.screen.blit(
                txt2, (WIDTH//2 - txt2.get_width()//2, HEIGHT//2 + 20))
            pygame.display.flip()
            self.clock.tick(FPS)

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_SPACE:
                        self.launch_ball()
                    if ev.key == pygame.K_n:
                        # manual next level
                        self.level += 1
                        self.spawn_level()
                        start_count = 2 if self.level >= 2 else 1
                        self.reset_ball(count=start_count)
                        bonus = min(2, MAX_BALLS - len(self.balls))
                        for _ in range(bonus):
                            bx = self.paddle.x + self.paddle.w // 2 + \
                                random.uniform(-20, 20)
                            by = self.paddle.y - 10
                            b = Ball(bx, by, random.uniform(-220, 220), -320)
                            self.balls.append(b)

            self.update(dt)

            self.screen.fill((12, 18, 35))

            for brick in self.bricks:
                brick.draw(self.screen)

            self.paddle.draw(self.screen)
            for b in self.balls:
                b.draw(self.screen)

            self.draw_hud()

            pygame.display.flip()


if __name__ == '__main__':
    Game().run()
