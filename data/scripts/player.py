import pygame


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False
        self.bullets = []
        self.pressed_key = None

    def set_pos(self):
        self.rect.x = (self.x - self.width // 2)
        self.rect.y = (self.y - self.height // 2)

    def change_offset(self, offset=None):
        if offset is None:
            offset = [0, 0]
        self.x -= offset[0]
        self.y -= offset[1]
        self.set_pos()

    def display(self, display, mouse_pos):
        self.change_offset()
        pygame.draw.rect(display, self.color,self.rect)