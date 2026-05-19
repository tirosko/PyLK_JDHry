import pygame-ce, sys
from pygame.locals import QUIT, KEYUP, K_ESCAPE, MOUSEMOTION, MOUSEBUTTONUP

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

global FPSCLOCK, DISPLAYSURF
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
mousex = 0  # used to store x coordinate of mouse event
mousey = 0  # used to store y coordinate of mouse event
pygame.display.set_caption("Memory Game")
mainBoard = getRandomizedBoard()
revealedBoxes = generateRevealedBoxesData(False)

while True:  # main game loop
    mouseClicked = False

    DISPLAYSURF.fill(BGCOLOR)  # drawing the window
    # drawBoard(mainBoard, revealedBoxes)

    for event in pygame.event.get():  # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)