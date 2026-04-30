"""
 Bounces a rectangle around the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/-GmKoaX2iMs
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the height and width of the screen
x_size = 1000
y_size = 500

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x =2
rect_change_y =2

size = [x_size, y_size]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if abs(rect_change_x) > 20:
        done = True
    if abs(rect_change_y) > 20:
        done = True

    # --- Logic
    # Move the rectangle starting point
    rect_x += rect_change_x
    rect_y += rect_change_y
    naraz = False

    # Bounce the ball if needed
    okraj_x = x_size - 50
    okraj_y = y_size - 50
    if rect_y > okraj_y or rect_y < 0:
        naraz = True
        rect_change_y = rect_change_y * -1
    if rect_x > okraj_x or rect_x < 0:
        naraz = True  
        rect_change_x = rect_change_x * -1

    if naraz:
        # print("Naraz!")
        if rect_change_x > 0:
            # print("Směr: doprava")
            rect_change_x = rect_change_x + 1
        elif rect_change_x < 0:
            # print("Směr: doleva")
            rect_change_x = rect_change_x - 1
        if rect_change_y > 0:
            # print("Směr: dolů")
            rect_change_y = rect_change_y + 1
        elif rect_change_y < 0:
            # print("Směr: nahoru")
            rect_change_y = rect_change_y - 1

    naraz = False

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    # pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()
