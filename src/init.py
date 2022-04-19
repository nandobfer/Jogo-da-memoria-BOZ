import pygame
from pygame.locals import *
# from pygame import mixer

resolution = (768/2, 1280/2)

# Initialize pygame
pygame.init()
# Title and Icon
pygame.display.set_caption("Memória")
icon = pygame.image.load('src/assets/icon.png')
pygame.display.set_icon(icon)