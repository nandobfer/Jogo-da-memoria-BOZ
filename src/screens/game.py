import pygame, init
from pygame.locals import *
from config import *

def start():
    # create a screen
    screen = pygame.display.set_mode(init.resolution, DOUBLEBUF, 16)

    # Background
    background = pygame.image.load(BACKGROUND).convert()
    background = pygame.transform.scale(background, init.resolution)

    # On game flag
    game = True

    # System Clock
    clock = pygame.time.Clock()

    # Game loop
    while game:
        # Getting mouse position = (x,y)
        mouse = pygame.mouse.get_pos()
        
        # Refresh Rate
        clock.tick(60)

        # Blit background
        screen.blit(background, (0, 0))

        # Event Loop
        for event in pygame.event.get():

            # Closing game window
            if event.type == pygame.QUIT:
                game = False

        
        # Update Screen
        pygame.display.update()