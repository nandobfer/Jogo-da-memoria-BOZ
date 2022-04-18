import pygame, init
from pygame import mixer
from pygame.locals import *

def start():
    # create a screen
    screen = pygame.display.set_mode(init.resolution, DOUBLEBUF, 16)

    # # Music
    # mixer.music.load('caminho')
    # mixer.music.play(-1)
    # mixer.music.set_volume(mixer.music.get_volume() / 2)

    # # Background
    # background = pygame.image.load('path').convert()
    # background = pygame.transform.scale(background, init.resolution)

    # Start Menu flag
    start_menu = True

    # System Clock
    clock = pygame.time.Clock()

    # Screen Loop
    while start_menu:

        # Getting mouse position = (x,y)
        mouse = pygame.mouse.get_pos()

        # Refresh Rate - FPS
        clock.tick(60)

        # Show Background
        # screen.blit(background, (0, 0))

        # Event Loop
        for event in pygame.event.get():

            # Closing game window
            if event.type == pygame.QUIT:
                start_menu = False

            # On mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # Quit Button
                # if quit.getMouse(mouse):
                    # Game.quitGame()

        # Draw Buttons (screen, mouse)
        # quit.draw(screen, mouse)
        # play.draw(screen, mouse)

        # Update Screen
        pygame.display.update()

        # Print mouse coordenates in console
        # print(mouse)