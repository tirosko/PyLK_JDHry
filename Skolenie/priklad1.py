# Growing Circle Project
# This program creates a Pygame window where a circle can be moved, resized,
# and have its color and border thickness adjusted using keyboard inputs.
# Controls:
# Arrow Keys: Move the circle up, down, left, right
# Z/X: Decrease/Increase circle radius
# 1/2: Increase/Decrease red component of fill color
# 3/4: Increase/Decrease green component of fill color
# 5/6: Increase/Decrease blue component of fill color
# B/N: Increase/Decrease border thickness
# Q: Quit the program
# https://github.com/tlcDataScience/pygame-learning/blob/main/Wiki/Lesson%205.md
import pygame

# Initialize Pygame
pygame.init()


# -------------------------------
# Set up the Pygame window
# -------------------------------
WINDOW_WIDTH = 600      # Window width in pixels
WINDOW_HEIGHT = 400     # Window height in pixels
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Growing Circle Project")

# -------------------------------
# Initial parameters for the circle
# -------------------------------
# Circle center (x, y) - start in the middle of the window
circle_center_x = WINDOW_WIDTH // 2
circle_center_y = WINDOW_HEIGHT // 2

# Circle radius - start with a radius of 50 pixels
circle_radius = 50

# Fill color for the circle (RGB) - start with red
fill_color = [255, 0, 0]

# Border thickness for the circle (0 means the circle is filled completely)
border_thickness = 0

# Border color for the circle - we will use black
border_color = (0, 0, 0)

# -------------------------------
# Helper function to keep values in range
# -------------------------------


def clamp(value, min_value, max_value):
    """Keep a value between a minimum and maximum value."""
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


# -------------------------------
# Main game loop
# -------------------------------
clock = pygame.time.Clock()  # Controls the frame rate
running = True

while running:
    # Fill the background with white
    WINDOW.fill((255, 255, 255))

    # -------------------------------
    # Process events (like key presses)
    # -------------------------------
    for event in pygame.event.get():
        # End the loop if the window is closed
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            # Press Q to quit the program
            if event.key == pygame.K_q:
                running = False

            # --------------------------------
            # Adjust the circle's position with arrow keys
            # --------------------------------
            if event.key == pygame.K_LEFT:
                circle_center_x -= 10  # Move left by 10 pixels
            if event.key == pygame.K_RIGHT:
                circle_center_x += 10  # Move right by 10 pixels
            if event.key == pygame.K_UP:
                circle_center_y -= 10  # Move up by 10 pixels
            if event.key == pygame.K_DOWN:
                circle_center_y += 10  # Move down by 10 pixels

            # --------------------------------
            # Adjust the circle's size (radius)
            # Use Z to decrease radius and X to increase radius
            # --------------------------------
            if event.key == pygame.K_z:
                circle_radius -= 5
                # Ensure the radius doesn't get too small
                if circle_radius < 5:
                    circle_radius = 5
            if event.key == pygame.K_x:
                circle_radius += 5

            # --------------------------------
            # Adjust the fill color of the circle
            # Use keys 1-6 to change red, green, blue values:
            #   1: Increase red, 2: Decrease red
            #   3: Increase green, 4: Decrease green
            #   5: Increase blue, 6: Decrease blue
            # --------------------------------
            if event.key == pygame.K_1:
                fill_color[0] = clamp(fill_color[0] + 5, 0, 255)
            if event.key == pygame.K_2:
                fill_color[0] = clamp(fill_color[0] - 5, 0, 255)
            if event.key == pygame.K_3:
                fill_color[1] = clamp(fill_color[1] + 5, 0, 255)
            if event.key == pygame.K_4:
                fill_color[1] = clamp(fill_color[1] - 5, 0, 255)
            if event.key == pygame.K_5:
                fill_color[2] = clamp(fill_color[2] + 5, 0, 255)
            if event.key == pygame.K_6:
                fill_color[2] = clamp(fill_color[2] - 5, 0, 255)

            # --------------------------------
            # Adjust the circle's border thickness
            # Use B to increase and N to decrease the border thickness
            # --------------------------------
            if event.key == pygame.K_b:
                border_thickness += 1
                # Ensure border thickness does not exceed the radius
                if border_thickness > circle_radius:
                    border_thickness = circle_radius
            if event.key == pygame.K_n:
                border_thickness -= 1
                if border_thickness < 0:
                    border_thickness = 0

    # -------------------------------
    # Draw the circle with the current parameters
    # -------------------------------
    # First, draw the filled circle using thickness 0 to fill it completely
    pygame.draw.circle(WINDOW, tuple(fill_color),
                       (circle_center_x, circle_center_y), circle_radius, 0)

    # Then, if a border is desired, draw the border on top of the filled circle
    if border_thickness > 0:
        pygame.draw.circle(WINDOW, border_color, (circle_center_x,
                           circle_center_y), circle_radius, border_thickness)

    # Update the display so we can see the new circle
    pygame.display.flip()

    # Limit the frame rate to 60 frames per second
    clock.tick(60)

# When the loop ends, quit Pygame
pygame.quit()
