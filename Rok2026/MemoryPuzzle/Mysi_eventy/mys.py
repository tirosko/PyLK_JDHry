import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# event.button hodnoty:
# 1 = ľavé tlačidlo
# 2 = stredné (koliesko)
# 3 = pravé
# 4 = koliesko hore
# 5 = koliesko dole
# 6 = bocne dolne tlačidlo
# 7 = bocne horne tlačidlo

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Klik:", event.pos, "tlačidlo:", event.button)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Klik:", event.pos)

        if event.type == pygame.MOUSEMOTION:
            print("Pohyb:", event.pos)

pygame.quit()
