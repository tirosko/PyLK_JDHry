import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Udalosti myši")

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("↓ Stlačené:", event.pos, "button:", event.button)

        if event.type == pygame.MOUSEBUTTONUP:
            print("↑ Pustené:", event.pos, "button:", event.button)

        if event.type == pygame.MOUSEMOTION:
            print("→ Pohyb:", event.pos, "rel:", event.rel, "buttons:", event.buttons)

pygame.quit()
