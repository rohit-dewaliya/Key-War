import pygame

from data.scripts.enemy import *

class EnemyManager:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.level = 1
        self.words = []
        self.enemies = []

        self.get_words()

    def get_words(self):
        with open('data/levels/level.txt', 'r') as file:
            self.words = file.readlines()[self.level - 1].split(",")
            self.words.pop()
        self.generate_enemies()

    def generate_enemies(self):
        for word in self.words:
            self.enemies.append(Enemy(self.screen_size, word))

    def display_enemies(self, display):
        for enemy in self.enemies:
            enemy.display(display)
