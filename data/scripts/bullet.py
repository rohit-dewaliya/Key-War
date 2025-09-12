import pygame
import math


class BulletManager:
    def __init__(self, screen_size, bullet):
        self.screen_size = screen_size
        self.bullets = []
        self.bullet = bullet

    def add_bullet(self, x, y, enemy):
        bullet = Bullet(x, y, enemy, self.bullet)
        self.bullets.append(bullet)

    def display(self, display):
        for index, bullet in enumerate(self.bullets):
            bullet.display(display)
            if 0 < bullet.get_distance() < 30:
                self.bullets.remove(bullet)
                bullet.enemy.word = bullet.enemy.word[1 : ]


class Bullet:
    def __init__(self, x, y, enemy, bullet):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 30
        self.bullet_anlge = 0
        self.enemy = enemy

        self.get_angle()

        self.bullet = pygame.transform.rotate(bullet, 180 - self.bullet_anlge)
        self.bullet_size = self.bullet.get_size()

    def get_angle(self):
        x = self.x - self.enemy.x
        y = self.y - self.enemy.y
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

    def get_distance(self):
        x = (self.x - self.enemy.x) ** 2
        y = (self.y - self.enemy.y) ** 2

        return int(math.sqrt(x) + math.sqrt(y))

    def display(self, display):
        display.blit(self.bullet, (self.x - self.bullet_size[0] // 2, self.y - self.bullet_size[1] // 2))
        self.new_coordinates()
        self.get_angle()