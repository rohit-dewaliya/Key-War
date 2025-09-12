import pygame
from pygame.locals import *

from data.scripts.clock import Clock
from data.scripts.font import Font
from data.scripts.image_functions import load_image, scale_image_size
from data.scripts.player import Player

from data.scripts.partices import *
from data.scripts.enemy_manager import *
from data.scripts.bullet import BulletManager


pygame.init()
pygame.mixer.init()

def load_sound(file_name):
    return pygame.mixer.Sound("data/sounds/" + file_name)

def play_sound(sound):
    pygame.mixer.Sound.play(sound)


class Game:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size, 0, 32)

        pygame.display.set_caption("Key War")
        pygame.display.set_icon(load_image('icon.png'))

        # Images------------------------------#
        self.background = load_image('background/stars.jpg')
        self.grid = scale_image_size(load_image('background/grid.png', 100), *self.size)
        self.gradient = scale_image_size(load_image('background/gradient.png'), *self.size)

        self.bullet = pygame.image.load('data/images/bullet.png').convert()
        self.bullet.set_colorkey((0, 0, 0))

        # Fonts-----------------------------#
        self.score_fonts = Font('small_font.png', (255, 255, 255), 2)

        # Music-----------------------------#
        # self.burst = load_sound('burst.wav')
        # self.buttonclick = load_sound('buttonclick.wav')
        # self.ballbounce = load_sound('ballbounce.wav')
        # self.rocksmash = load_sound('rocksmash.wav')
        #
        # pygame.mixer.music.load('data/sounds/background music.mp3')
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.4)

        self.clock = Clock(30)
        self._game = True
        self.game_start = False

        # Text----------------#
        # self.score_font = Font('small_font.png', (255, 255, 255), 4)

        # Particles--------------------------------------------------------#
        load_particle_images('data/images/particles/')
        self.particles = []

        self.player_size = [20, 40]
        self.player = Player((self.size[0] - self.player_size[0]) // 2, (self.size[1] - self.player_size[1] - 10),
                             *self.player_size)

        # Enemies-------------------------#
        self.enemy_manager = EnemyManager(self.size)
        self.background_pos = 0

        self.bullet_manager = BulletManager(self.size, self.bullet)

    def main(self):
        while self._game:

            mouse_pos = pygame.mouse.get_pos()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.grid, (0, self.background_pos))
            self.screen.blit(self.grid, (0, self.background_pos - self.size[1]))
            self.screen.blit(self.gradient, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
            self.background_pos += 1
            if self.background_pos >= self.size[1]:
                self.background_pos = 0

            self.bullet_manager.display(self.screen)
            self.player.display(self.screen, mouse_pos)
            self.enemy_manager.display_enemies(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._game = False

                if event.type == pygame.KEYDOWN:
                    self.player.pressed_key = event.unicode
                    if self.enemy_manager.check_word_locked(self.player.pressed_key):
                        self.bullet_manager.add_bullet(self.player.x, self.player.y, self.enemy_manager.locked_enemy)

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass

            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    size = [600, 700]
    Enemy.screen_size = size
    game = Game(size)
    game.main()
