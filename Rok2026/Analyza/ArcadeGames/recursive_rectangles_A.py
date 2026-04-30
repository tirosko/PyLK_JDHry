"""
 Recursively draw rectangles.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Store rectangles to animate
rectangles_to_draw = []


def recursive_draw(x, y, width, height):
    """ Recursive rectangle function - stores rectangles for animation. """
    rectangles_to_draw.append([x, y, width, height])

    # Is the rectangle wide enough to draw again?
    if(width > 14):
        # Scale down
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        # Recursively draw again
        recursive_draw(x, y, width, height)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
# First, collect all rectangles to draw
recursive_draw(0, 0, 700, 500)

# Animation index
current_index = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the screen background
    screen.fill(WHITE)

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # Draw rectangles up to current animation index
    for i in range(current_index + 1):
        rect = rectangles_to_draw[i]
        pygame.time.delay(50)  # Pause for animation effect
        pygame.draw.rect(screen, RED, rect, 1)

    # Animate: advance to next rectangle every few frames
    if current_index < len(rectangles_to_draw) - 1:
        current_index += 1
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()