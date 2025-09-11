import pygame
import math


class BulletManager:
    def __init__(self, screen_size, bullet):
        self.screen_size = screen_size
        self.bullets = []
        self.bullet = bullet

    def add_bullet(self, x, y, mouse_pos):
        bullet = Bullet(x, y, mouse_pos, self.bullet)
        self.bullets.append(bullet)

    def display(self, display):
        for index, bullet in enumerate(self.bullets):
            bullet.display(display)
            if 0 > bullet.x or bullet.x > self.screen_size[0] or 0 > bullet.y or bullet.y > self.screen_size[1]:
                self.bullets.remove(bullet)


class Bullet:
    def __init__(self, x, y, mouse_pos, bullet):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 30
        self.bullet_anlge = 0

        self.get_angle(mouse_pos)

        self.bullet = pygame.transform.rotate(bullet, 180 - self.bullet_anlge)
        self.bullet_size = self.bullet.get_size()

    def get_angle(self, mouse_pos):
        x = self.x - mouse_pos[0]
        y = self.y - mouse_pos[1]
        self.bullet_anlge = math.atan2(y, x)

        self.bullet_anlge = math.degrees(self.bullet_anlge) + 180

        self.angle = math.radians(self.bullet_anlge)

    def find_coordinates(self):
        y = self.speed * math.sin(self.angle)
        x = self.speed * math.cos(self.angle )
        return [x, y]

    def new_coordinates(self):
        coors = self.find_coordinates()
        self.x += coors[0]
        self.y += coors[1]

    def display(self, display):
        display.blit(self.bullet, (self.x - self.bullet_size[0] // 2, self.y - self.bullet_size[1] // 2))
        self.new_coordinates()