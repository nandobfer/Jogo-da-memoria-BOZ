import pygame, config, init

class Button:
    # text, size = (width, height), img = string ("path/file.png")
    def __init__(self, text, size, img, downed_img):
        self.text = config.text.render(text, True, (170, 170, 170))
        self.text_mouse = config.text.render(text, True, (255, 255, 255))
        self.size = size
        self.width = size[0]
        self.height = size[1]
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, self.size)
        self.downed_img = pygame.image.load(downed_img).convert_alpha()
        self.downed_img = pygame.transform.scale(self.downed_img, self.size)
        self.offset_x = 0
        self.offset_y = 0
        self.x = 0
        self.y = 0
        self.position = (0,0)
        self.clicked = False

    # set size
    def setSize(self, x, y):
        self.size = (x,y)
        self.width = x
        self.height = y

    # set offset for alpha distances in images
    def setOffset(self, x, y):
        self.offset_x = x
        self.offset_y = y

    # set position for easy access
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (x,y)

    # mouse = (x, y), position = (x, y)
    def getMouse(self, mouse):
        if self.x - self.offset_x <= mouse[0] <= self.x - self.offset_x + self.width and self.y <= mouse[1] <= self.y - 2 * self.offset_y + self.height:
            return True

    # screen, mouse = (x,y)
    def draw(self, screen, mouse):
        if not self.clicked:
            screen.blit(self.img, (self.x - self.offset_x, self.y - self.offset_y))
        else:
            screen.blit(self.downed_img, (self.x - self.offset_x, self.y - self.offset_y))



