import pygame
import sys
import math

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Garden Scene")

# Colors
SKY_BLUE = (135, 206, 235)
CLOUD_BLUE = (200, 220, 255)   # light bluish
WHITE    = (255, 255, 255)        # for clouds
YELLOW   = (255, 255, 0)
GREEN    = (0, 128, 0)
BROWN    = (139, 69, 19)
RED      = (255, 0, 0)
PURPLE   = (128, 0, 128)
MAGENTA  = (255, 0, 255)          # car body

def draw_house(screen):
    # Walls
    pygame.draw.rect(screen, BROWN, (100, 300, 200, 150))
    # Roof
    pygame.draw.polygon(screen, RED, [(100, 300), (200, 200), (300, 300)])
    
    # Door
    pygame.draw.rect(screen, (101, 50, 15), (180, 380, 40, 70))  # Dark brown door
    # Door handle
    pygame.draw.circle(screen, YELLOW, (218, 415), 3)
    
    # Window 1 (left)
    pygame.draw.rect(screen, (135, 206, 235), (130, 330, 40, 40))  # Light blue glass
    pygame.draw.line(screen, BROWN, (150, 330), (150, 370), 2)  # Vertical frame
    pygame.draw.line(screen, BROWN, (130, 350), (170, 350), 2)  # Horizontal frame
    
    # Window 2 (right)
    pygame.draw.rect(screen, (135, 206, 235), (230, 330, 40, 40))
    pygame.draw.line(screen, BROWN, (250, 330), (250, 370), 2)
    pygame.draw.line(screen, BROWN, (230, 350), (270, 350), 2)

def draw_tree(screen):
    # Trunk
    pygame.draw.rect(screen, BROWN, (500, 350, 30, 100))
    # Foliage
    pygame.draw.circle(screen, GREEN, (515, 320), 50)
    # Apples
    pygame.draw.circle(screen, RED, (510, 300), 5)
    pygame.draw.circle(screen, RED, (500, 330), 5)
    pygame.draw.circle(screen, RED, (495, 353), 5)
    pygame.draw.circle(screen, RED, (530, 320), 5)

def draw_flowers(screen):
    # Flower 1
    pygame.draw.line(screen, GREEN, (50, 480), (50, 430), 2)
    pygame.draw.circle(screen, YELLOW, (50, 425), 10)
    # Flower 2
    pygame.draw.line(screen, GREEN, (400, 480), (400, 430), 2)
    pygame.draw.circle(screen, PURPLE, (400, 425), 10)
    # Flower 3
    pygame.draw.line(screen, GREEN, (350, 480), (350, 430), 2)
    pygame.draw.circle(screen, RED, (350, 425), 10)
    # Flower 4
    pygame.draw.line(screen, GREEN, (450, 480), (450, 430), 2)
    pygame.draw.circle(screen, YELLOW, (450, 425), 10)

def draw_sun(screen):
    cx, cy, r = 700, 100, 50
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        # make the rays longer by extending beyond the radius more
        x = cx + int(math.cos(rad) * (r + 40))   # was r + 20
        y = cy + int(math.sin(rad) * (r + 40))
        pygame.draw.line(screen, YELLOW, (cx, cy), (x, y), 3)

    pygame.draw.circle(screen, YELLOW, (cx, cy), r)

def draw_cloud(screen, x, y):
    pygame.draw.circle(screen, CLOUD_BLUE, (x,   y),   20)
    pygame.draw.circle(screen, CLOUD_BLUE, (x+25, y+10), 25)
    pygame.draw.circle(screen, CLOUD_BLUE, (x+50, y),   20)

def draw_clouds(screen):
    draw_cloud(screen, 100, 80)
    draw_cloud(screen, 300, 60)
    draw_cloud(screen, 500, 90)

def draw_car(screen):
    # body position
    body_x, body_y = 600, 390
    body_w, body_h = 160, 60

    pygame.draw.rect(screen, MAGENTA, (body_x, body_y, body_w, body_h))

    # wheels: centre them under the body, a few pixels below the bottom edge
    wheel_y = body_y + body_h + 5          # 5‑px gap below the car
    pygame.draw.circle(screen, (0, 0, 0), (body_x + 30,  wheel_y), 14)
    pygame.draw.circle(screen, (0, 0, 0), (body_x + 130, wheel_y), 14)

    # windows – still inside the body rectangle
    pygame.draw.rect(screen, SKY_BLUE, (body_x + 20,  body_y + 10, 40, 30))
    pygame.draw.rect(screen, SKY_BLUE, (body_x + 90,  body_y + 10, 40, 30))

    # no dividing line this time

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(SKY_BLUE)
    draw_sun(screen)
    draw_clouds(screen)

    # grass
    pygame.draw.rect(screen, GREEN, (0, 450, W, 150))

    draw_house(screen)
    draw_tree(screen)
    draw_car(screen)
    draw_flowers(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()