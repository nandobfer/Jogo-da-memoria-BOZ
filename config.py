import pygame, init

# UI 
BACKGROUND = 'src/assets/ui/background.jpg'
PLAY = 'src/assets/ui/buttons/play.png'
DOWNED_PLAY ='src/assets/ui/buttons/downed_play.png'
PLAY_SIZE = (992/4,258/4)
QUIT = 'src/assets/ui/buttons/quit.png'
DOWNED_QUIT = 'src/assets/ui/buttons/downed_quit.png'
QUIT_SIZE = (992/4,258/4)

# Game
images = []
for i in range(20):
    images.append(pygame.image.load('src/assets/drawings/Pic'+str(i+1)+'.png'))

# text fonts
small_text = pygame.font.Font('src/assets/JOSEFINSANS-VARIABLEFONT_WGHT.TTF', int(0.02 * init.resolution[0]))
text = pygame.font.Font('src/assets/JOSEFINSANS-VARIABLEFONT_WGHT.TTF', int(0.04 * init.resolution[0]))
big_text = pygame.font.Font('src/assets/JOSEFINSANS-VARIABLEFONT_WGHT.TTF', int(0.08 * init.resolution[0]))

