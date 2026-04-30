"""
 Bounces a rectangle around the screen.
 Refactoring of bouncing_rectangle.py to use classes.
 Zamyslenie
 
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
RED = (255, 0, 0)


class BouncingRectangle:
    def __init__(self, x, y, width=50, height=50, change_x=2, change_y=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.change_x = change_x
        self.change_y = change_y

    def update(self, boundary_width, boundary_height):
        self.x += self.change_x
        self.y += self.change_y

        if self.y < 0 or self.y > boundary_height - self.height:
            self.change_y *= -1
        if self.x < 0 or self.x > boundary_width - self.width:
            self.change_x *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, [
                         self.x, self.y, self.width, self.height])
        pygame.draw.rect(
            surface, RED, [self.x + 10, self.y + 10, self.width - 20, self.height - 20])


class BouncingRectangleGame:
    def __init__(self, width=700, height=500, title="Bouncing Rectangle"):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.done = False
        self.boundary_width = width
        self.boundary_height = height
        self.rectangle = BouncingRectangle(50, 50)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def run(self):
        while not self.done:
            self.process_events()
            self.rectangle.update(self.boundary_width, self.boundary_height)
            self.screen.fill(BLACK)
            self.rectangle.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = BouncingRectangleGame()
    game.run()
