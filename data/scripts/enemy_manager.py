import pygame

from data.scripts.enemy import *
from data.scripts.font import *
from data.scripts.partices import Particle

class EnemyManager:
    def __init__(self, screen_size, sound, hurt_sound):
        self.screen_size = screen_size
        self.words = []
        self.enemies = []
        self.level = 0
        self.max_levels = 42
        self.level_change = True
        self.level_change_time = 300
        self.level_time = 0
        self.level_time_remaining = 0
        self.sound = sound
        self.hurt_sound = hurt_sound
        self.word_counter = 0

        self.lock_enemy = False
        self.locked_enemy = False
        self.word_lock = False
        self.locked_word = ""

        self.level_fonts = Font('small_font.png', (255, 255, 255), 10)
        self.level_font_width = 0
        self.level_font_height = self.level_fonts.image_height

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
            self.word_counter += 1
            return True
        return False

    def check_word_locked(self, key):
        matched = False
        if not self.word_lock:
            enemies = []
            for enemy in self.enemies:
                if len(enemy.word) > 0 and enemy.word[0] == key:
                    enemies.append(enemy)

            if enemies:
                enemy = max(enemies, key=lambda x: x.y)
                self.locked_enemy = enemy
                self.word_lock = True
                self.locked_word = enemy.word

        if self.word_lock:
            if self.locked_word[0] == key:
                self.locked_word = self.locked_word[1:]
                matched = True

            if len(self.locked_word) == 0:
                self.locked_word = None
                self.word_lock = False

        return matched

    def calculae_defeat(self):
        for index, enemy in enumerate(self.enemies):
            if enemy.y > self.screen_size[1]:
                self.lock_enemy = None
                self.locked_word = None
                self.word_lock = False
                self.enemies.pop(index)
                self.hurt_sound.play()
                return True
        return False

    def display_enemies(self, display, particles):
        if not self.level_change:
            for index, enemy in enumerate(self.enemies):
                enemy.display(display)
                if self.remove_enemies(enemy):
                    self.enemies.remove(enemy)
                    self.sound.play()
                    for d in range(0, 100):
                        particles.append(
                            Particle([enemy.x + enemy.size[0] // 2 + random.randint(-10, 10), enemy.y + enemy.size[1]
                             // 2 + random.randint(-10,10)], 'p', [random.randint(-2, 2), 5], 0.8, 0, random.choice(
                                [(255, 0, 0), (255, 255, 0)]), True))
        else:
            self.level_fonts.display_fonts_with_border(display, "Level " + str(self.level), [(self.screen_size[0] -
                                                                                 self.level_font_width) // 2,
                                                                                 (self.screen_size[1] -
                                                                                  self.level_font_height) // 2], 10,
                                                       (0, 162, 232), 2)
            self.level_time += 10
            if self.level_time - self.level_time_remaining >= self.level_change_time:
                self.level_change = False

        if len(self.enemies) == 0:
            self.level += 1
            self.get_words()

            self.level_font_width = self.level_fonts.get_width("Level " + str(self.level))

            if not self.level_change:
                self.level_change = True
                self.level_time_remaining = self.level_time = pygame.time.get_ticks()

            if self.level > self.max_levels:
                self.level = self.max_levels - 1
