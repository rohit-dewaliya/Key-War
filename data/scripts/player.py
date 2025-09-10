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
        # pygame.draw.circle(display, (255, 255, 0), (self.x, self.y), 1)

        # if self.clicked:
        #     # x = self.x - mouse_pos[0]
        #     # y = self.y - mouse_pos[1]
        #     # angle = math.atan2(y, x)
        #     #
        #     #
        #     # angle = math.degrees(angle) + 180
        #     # angle = math.radians(angle)
        #     bullet = Bullet(self.x, self.y, mouse_pos)
        #     self.bullets.append(bullet)
        #     print(self.bullets)
        #     self.clicked = False
        #
        # for bullet in self.bullets:
        #     bullet.display(display)