"""
 Bounces a rectangle around the screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/-GmKoaX2iMs
"""
import os
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

rect_width = 70
rect_height = 70

# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2

# Premenná pre zastavenie pohybu
paused = False

script_dir = os.path.dirname(os.path.abspath(__file__))
sound_folder = os.path.join(script_dir, 'Sounds')
sound_path = os.path.join(sound_folder, 'match1.wav')
rect_sound = pygame.mixer.Sound(sound_path)

size = [x_size, y_size]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Definícia tlačidla (vľavo hore)
button_rect = pygame.Rect(10, 10, 50, 50)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # Kontrola kliknutia myšou na tlačidlo
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                paused = not paused  # Prepne stav medzi zastaveným a spusteným

    if not paused:
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
        okraj_x = x_size - rect_width
        okraj_y = y_size - rect_height
        if rect_y > okraj_y or rect_y < 0:
            naraz = True
            rect_change_y = rect_change_y * -1
        if rect_x > okraj_x or rect_x < 0:
            naraz = True  
            rect_change_x = rect_change_x * -1

        if naraz:
            rect_sound.play()
            if rect_change_x > 0:
                rect_change_x = rect_change_x + 1
            elif rect_change_x < 0:
                rect_change_x = rect_change_x - 1
            if rect_change_y > 0:
                rect_change_y = rect_change_y + 1
            elif rect_change_y < 0:
                rect_change_y = rect_change_y - 1
        
        naraz = False

    # --- Drawing
    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, rect_width, rect_height])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, rect_width - 20, rect_height - 20])

    # Vykreslenie tlačidla Stop/Play
    pygame.draw.rect(screen, WHITE, button_rect, 2) # Obrys tlačidla
    if paused:
        # Vykresli zelený trojuholník (Play)
        pygame.draw.polygon(screen, GREEN, [[20, 15], [20, 55], [50, 35]])
    else:
        # Vykresli červený štvorec (Stop)
        pygame.draw.rect(screen, RED, [20, 20, 30, 30])

    # --- Wrap-up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close everything down
pygame.quit()