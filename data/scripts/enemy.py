import random
import pygame

from data.scripts.font import Font
from data.scripts.image_functions import load_image

text = Font('small_font.png', (255, 0, 0), 2)

class Enemy:
    def __init__(self, screen_size, word = ""):
        self.x = 0
        self.y = 0
        self.speed = random.randint(1, 6)
        self.image = random.choice([load_image('enemy_1.png'), load_image('enemy_2.png')])
        self.size = self.image.get_size()
        self.screen_size = screen_size
        self.word = word
        self.set_initial_pos()
        self.word_width = 0
        self.word_position = [0, 0]
        self.set_position()

    def set_position(self):
        self.word_width = text.get_width(self.word)
        self.word_position = [self.size[0] // 2 + self.x - self.word_width // 2, self.y + self.size[1] + 10]

    def set_initial_pos(self):
        self.x = random.randint(50, self.screen_size[0] - 50)
        self.y = random.randint(-100, -10)

    def move(self):
        self.y += self.speed

    def display(self, display):
        self.set_position()
        display.blit(self.image, [self.x, self.y])
        # pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, *self.size))
        text.display_fonts(display, self.word, [self.word_position[0], self.y + self.size[1] + 10])
        self.move()
