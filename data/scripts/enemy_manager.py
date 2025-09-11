import pygame

from data.scripts.enemy import *

class EnemyManager:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.level = 1
        self.words = []
        self.enemies = []

        self.lock_enemy = False
        self.locked_enemy = False
        self.locked_word = ""

        self.get_words()

    def get_words(self):
        with open('data/levels/level.txt', 'r') as file:
            self.words = file.readlines()[self.level - 1].split(",")
            self.words.pop()
        self.generate_enemies()

    def generate_enemies(self):
        for word in self.words:
            self.enemies.append(Enemy(self.screen_size, word))

    def check_word_locked(self, key):
        matched = False

        for enemy in self.enemies:
            if not self.lock_enemy:
                if enemy.word[0] == key:
                    self.lock_enemy = True
                    self.locked_enemy = enemy
                    self.locked_word = enemy.word

        if self.lock_enemy:
            if self.locked_enemy.word[0] == key:
                self.locked_enemy.word = self.locked_word[1 : ]
                self.locked_word = self.locked_word[1:]
                matched = True

            if len(self.locked_word) == 0:
                self.enemies.remove(self.locked_enemy)
                self.lock_enemy = False
                self.locked_word = ""
                self.locked_enemy = None

        return matched

    def display_enemies(self, display):
        for enemy in self.enemies:
            enemy.display(display)