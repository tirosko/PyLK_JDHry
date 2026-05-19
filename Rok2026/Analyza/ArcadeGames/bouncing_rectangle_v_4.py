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
BLUE = (0, 0, 255)

pygame.init()

# Set the height and width of the screen
x_size = 1000
y_size = 500

# Starting position of the rectangle (upravený štart pod čiarou)
rect_x = 50
rect_y = 80

rect_width = 70
rect_height = 70

# Speed and direction of rectangle
rect_change_x = 2
rect_change_y = 2

# Stavové premenné
paused = False

script_dir = os.path.dirname(os.path.abspath(__file__))
sound_folder = os.path.join(script_dir, 'Sounds')
sound_path = os.path.join(sound_folder, 'match1.wav')

# Ošetrenie načítania zvuku
try:
    rect_sound = pygame.mixer.Sound(sound_path)
except:
    rect_sound = None

size = [x_size, y_size]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Definícia tlačidiel
pause_button_rect = pygame.Rect(10, 10, 50, 50)
restart_button_rect = pygame.Rect(70, 10, 50, 50)

# Čiara pod tlačidlami (na y = 70)
line_y = 70

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kliknutie na Stop/Play
            if pause_button_rect.collidepoint(event.pos):
                paused = not paused
            
            # Kliknutie na Restart
            if restart_button_rect.collidepoint(event.pos):
                rect_x = 50
                rect_y = 80
                rect_change_x = 2
                rect_change_y = 2
                paused = False

    if not paused:
        if abs(rect_change_x) > 20:
            done = True
        if abs(rect_change_y) > 20:
            done = True

        # --- Logic
        rect_x += rect_change_x
        rect_y += rect_change_y
        naraz = False

        okraj_x = x_size - rect_width
        okraj_y = y_size - rect_height

        # Kontrola kolízie s okrajmi
        if rect_x > okraj_x or rect_x < 0:
            naraz = True  
            rect_change_x = rect_change_x * -1

        # Kontrola kolízie s dolným okrajom A NOVOU ČIAROU HORE
        if rect_y > okraj_y:
            naraz = True
            rect_change_y = rect_change_y * -1
            
        elif rect_y < line_y: # Toto zabráni vstupu k tlačidlám
            rect_y = line_y
            naraz = True
            rect_change_y = rect_change_y * -1

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
    screen.fill(BLACK)

    # Kreslenie deliacej čiary pod tlačidlami
    pygame.draw.line(screen, WHITE, (0, line_y), (x_size, line_y), 2)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, rect_width, rect_height])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, rect_width - 20, rect_height - 20])

    # Kreslenie Stop/Play tlačidla
    pygame.draw.rect(screen, WHITE, pause_button_rect, 2)
    if paused:
        pygame.draw.polygon(screen, GREEN, [[20, 15], [20, 55], [45, 35]])
    else:
        pygame.draw.rect(screen, RED, [20, 20, 30, 30])

    # Kreslenie Restart tlačidla
    pygame.draw.rect(screen, WHITE, restart_button_rect, 2)
    pygame.draw.circle(screen, BLUE, (95, 35), 15, 3)

    # --- Wrap-up
    clock.tick(60)
    pygame.display.flip()

pygame.quit()