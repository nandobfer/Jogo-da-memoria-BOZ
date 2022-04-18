import pygame
from pygame.locals import *
# from pygame import mixer

resolution = (1024, 768)

# Initialize pygame
pygame.init()
# Title and Icon
pygame.display.set_caption("Memória")
icon = pygame.image.load('src/assets/icon.png')
pygame.display.set_icon(icon)