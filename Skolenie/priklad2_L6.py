import pygame

# Initialize Pygame
pygame.init()

# -------------------------------
# Window Settings
# -------------------------------
WIDTH = 500            # Window width in pixels
HEIGHT = 300           # Window height in pixels
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Scoreboard - Raw")

# -------------------------------
# Define Colors
# -------------------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# -------------------------------
# Score Limits and Initial Scores
# -------------------------------
MAX_SCORE = 20
player1 = 0
player2 = 0

# -------------------------------
# Helper Function
# -------------------------------


def clamp(value, min_val, max_val):
    """Ensure the value stays between min_val and max_val."""
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    else:
        return value

# -------------------------------
# Scoreboard Class for Raw Functionality
# -------------------------------


class Scoreboard:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Set up a font using the default freesansbold.ttf at size 32
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        # Row 1: Title ("Scoreboard") centered at the top
        self.titleSurface = self.font.render("Scoreboard", True, BLACK)
        self.titleRect = self.titleSurface.get_rect(center=(WIDTH // 2, 30))

        # Row 2: Player Labels
        self.label1Surface = self.font.render("Player 1", True, BLACK)
        self.label1Rect = self.label1Surface.get_rect(
            center=(int(WIDTH * 0.25), 60))

        self.label2Surface = self.font.render("Player 2", True, BLACK)
        self.label2Rect = self.label2Surface.get_rect(
            center=(int(WIDTH * 0.75), 60))

        # Row 3: Score Texts (these will be updated every frame)
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(
            center=(int(WIDTH * 0.25), 120))

        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(
            center=(int(WIDTH * 0.75), 120))

        # Row 3: Interactive Bar (a stacked bar) will be drawn in the center
        self.bar_width = 150
        self.bar_height = 30
        # The bar is centered horizontally at 50% of WIDTH and vertically at 120 pixels
        self.bar_rect = pygame.Rect(WIDTH // 2 - self.bar_width // 2,
                                    120 - self.bar_height // 2, self.bar_width, self.bar_height)

    def draw(self, surface):
        # Draw the title and labels
        surface.blit(self.titleSurface, self.titleRect)
        surface.blit(self.label1Surface, self.label1Rect)
        surface.blit(self.label2Surface, self.label2Rect)

        # Update the score texts to match the current scores
        self.score1Surface = self.font.render(str(self.p1), True, BLACK)
        self.score1Rect = self.score1Surface.get_rect(
            center=(int(WIDTH * 0.25), 120))
        self.score2Surface = self.font.render(str(self.p2), True, BLACK)
        self.score2Rect = self.score2Surface.get_rect(
            center=(int(WIDTH * 0.75), 120))

        # Draw the score texts
        surface.blit(self.score1Surface, self.score1Rect)
        surface.blit(self.score2Surface, self.score2Rect)

        # Draw the interactive stacked bar in the center
        # Draw a black border around the bar
        pygame.draw.rect(surface, BLACK, self.bar_rect, 2)

        # Calculate the ratio for the stacked bar
        total = self.p1 + self.p2
        if total == 0:
            ratio = 0.5  # Split evenly if both scores are zero
        else:
            ratio = self.p1 / total
        # Calculate widths for each part of the bar
        p1_bar_width = int(ratio * self.bar_width)
        p2_bar_width = self.bar_width - p1_bar_width

        # Draw Player 1's portion (red) on the left
        left_bar_rect = pygame.Rect(
            self.bar_rect.x, self.bar_rect.y, p1_bar_width, self.bar_height)
        pygame.draw.rect(surface, RED, left_bar_rect)
        # Draw Player 2's portion (blue) on the right
        right_bar_rect = pygame.Rect(
            self.bar_rect.x + p1_bar_width, self.bar_rect.y, p2_bar_width, self.bar_height)
        pygame.draw.rect(surface, BLUE, right_bar_rect)


# -------------------------------
# Main Game Loop for Raw Functionality
# -------------------------------
clock = pygame.time.Clock()
running = True

while running:
    WINDOW.fill(WHITE)  # Fill background with white

    # Process user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Quit the program when SPACE is pressed
            if event.key == pygame.K_SPACE:
                running = False
            # Increase Player 1's score with A (up to MAX_SCORE)
            if event.key == pygame.K_a:
                if player1 < MAX_SCORE:
                    player1 += 1
            # Increase Player 2's score with S
            if event.key == pygame.K_s:
                if player2 < MAX_SCORE:
                    player2 += 1
            # Decrease Player 1's score with Z (not below 0)
            if event.key == pygame.K_z:
                if player1 > 0:
                    player1 -= 1
            # Decrease Player 2's score with X
            if event.key == pygame.K_x:
                if player2 > 0:
                    player2 -= 1
            # Reset scores with R
            if event.key == pygame.K_r:
                player1 = 0
                player2 = 0

    # Create a Scoreboard object with the current scores
    scoreboard = Scoreboard(player1, player2)
    scoreboard.draw(WINDOW)

    # Update the display and control frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
