import pygame

from data.scripts.enemy import *

class EnemyManager:
    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.level = 1
        self.words = []
        self.enemies = []
        self.max_levels = 42

        self.lock_enemy = False
        self.locked_enemy = False
        self.word_lock = False
        self.locked_word = ""

        self.get_words()

    def get_words(self):
        with open('data/levels/level.txt', 'r') as file:
            self.data = file.readlines()
            self.words = self.data[self.level - 1].split(",")
            self.words.pop()
        self.generate_enemies()

    def generate_enemies(self):
        for word in self.words:
            self.enemies.append(Enemy(self.screen_size, word))

    def remove_enemies(self, enemy):
        if len(enemy.word) == 0:
            return True
        return False

    def check_word_locked(self, key):
        matched = False
        if not self.word_lock:
            for enemy in self.enemies:
                if len(enemy.word) > 0 and enemy.word[0] == key:
                    self.locked_enemy = enemy
                    self.word_lock = True
                    self.locked_word = enemy.word
                    print(self.locked_word, self.word_lock)

        if self.word_lock:
            if self.locked_word[0] == key:
                self.locked_word = self.locked_word[1:]
                matched = True

            if len(self.locked_word) == 0:
                self.locked_word = None
                self.word_lock = False

        return matched

    def display_enemies(self, display):
        for index, enemy in enumerate(self.enemies):
            enemy.display(display)
            if self.remove_enemies(enemy):
                self.enemies.remove(enemy)

        if len(self.enemies) == 0:
            self.level += 1
            self.get_words()
            if self.level > self.max_levels:
                self.level = self.max_levels - 1