import pygame
import math


class BulletManager:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.bullets = []

    def add_bullet(self, x, y, mouse_pos):
        bullet = Bullet(x, y, mouse_pos)
        self.bullets.append(bullet)

    def display(self, display):
        for index, bullet in enumerate(self.bullets):
            bullet.display(display)
            if 0 > bullet.x or bullet.x > self.screen_size[0] or 0 > bullet.y or bullet.y > self.screen_size[1]:
                self.bullets.remove(bullet)


class Bullet:
    def __init__(self, x, y, mouse_pos):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 15

        self.get_angle(mouse_pos)

    def get_angle(self, mouse_pos):
        x = self.x - mouse_pos[0]
        y = self.y - mouse_pos[1]
        angle = math.atan2(y, x)

        angle = math.degrees(angle) + 180
        self.angle = math.radians(angle)

    def find_coordinates(self):
        y = self.speed * math.sin(self.angle)
        x = self.speed * math.cos(self.angle )
        return [x, y]

    def new_coordinates(self):
        coors = self.find_coordinates()
        self.x += coors[0]
        self.y += coors[1]

    def display(self, display):
        pygame.draw.circle(display, (255,255,255), (self.x, self.y), 5)
        self.new_coordinates()