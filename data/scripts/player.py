import pygame


class Player:
    def __init__(self, x, y, width, height, image):
        self.x = x // 2
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        print(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)
        self.life = 5
        self.life_pos = [10, 10]
        self.life_image = pygame.image.load("data/images/life.png").convert()
        self.life_image_size = self.life_image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False
        self.bullets = []
        self.pressed_key = None

    def set_pos(self):
        self.rect.x = self.x - (self.width // 2)
        self.rect.y = self.y - (self.height // 2)

    def change_offset(self, offset=None):
        if offset is None:
            offset = [0, 0]
        self.x -= offset[0]
        self.y -= offset[1]
        self.set_pos()

    def display_life(self, display):
        x = self.life_pos[0]
        for i in range(self.life):
            display.blit(self.life_image, [x, self.life_pos[1]])
            x += self.life_image_size[0]
            x += 5 if i < self.life - 1 else 0

    def display(self, display, mouse_pos):
        self.change_offset()
        display.blit(self.image, [self.rect.x, self.rect.y])


        # pygame.draw.rect(display, self.color,self.rect)