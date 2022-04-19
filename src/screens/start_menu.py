import pygame, init, sys, screens.game
from pygame import mixer
from pygame.locals import *
from entities.Button import Button
from config import *

def start():
    # create a screen
    screen = pygame.display.set_mode(init.resolution, DOUBLEBUF, 16)

    # # Music
    # mixer.music.load('caminho')
    # mixer.music.play(-1)
    # mixer.music.set_volume(mixer.music.get_volume() / 2)

    # Background
    background = pygame.image.load(BACKGROUND).convert()
    background = pygame.transform.scale(background, init.resolution)

    # Start Menu flag
    start_menu = True

    # System Clock
    clock = pygame.time.Clock()

    # Play Button
    play = Button("Play", PLAY_SIZE, PLAY, DOWNED_PLAY)
    # play.setOffset(10,60)
    play.setPosition(70, 400)

    # Quit Button
    quit = Button("Quit", QUIT_SIZE, QUIT, DOWNED_QUIT)
    quit.setPosition(70, 500)

    # Screen Loop
    while start_menu:

        # Getting mouse position = (x,y)
        mouse = pygame.mouse.get_pos()

        # Refresh Rate - FPS
        clock.tick(60)

        # Show Background
        screen.blit(background, (0, 0))

        # Event Loop
        for event in pygame.event.get():

            # Closing game window
            if event.type == pygame.QUIT:
                start_menu = False

            # On mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Quit Button
                if quit.getMouse(mouse):
                    quit.clicked = True
                # Play Button
                if play.getMouse(mouse):
                    play.clicked = True

            # On mouse button up
            if event.type == pygame.MOUSEBUTTONUP:
                # Quit Button
                if quit.getMouse(mouse):
                    quit.clicked = False
                    sys.exit()
                # Play Button
                if play.getMouse(mouse):
                    play.clicked = False
                    screens.game.start()
                    start_menu = False

        # Draw Buttons (screen, mouse)
        quit.draw(screen, mouse)
        play.draw(screen, mouse)
        # Check undowned buttons
        if not quit.getMouse(mouse):
            quit.clicked = False
        if not play.getMouse(mouse):
            play.clicked = False

        # Update Screen
        pygame.display.update()

        # Print mouse coordenates in console
        print(mouse)