import pygame
import webbrowser

from pygame.locals import *

from data.scripts.clock import Clock
from data.scripts.font import Font
from data.scripts.player import Player

from data.scripts.partices import *
from data.scripts.enemy_manager import *
from data.scripts.bullet import BulletManager


pygame.init()
pygame.mixer.init()

from data.scripts.image_functions import load_image, scale_image_size

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

        self.button_size = 5
        self.play_button = scale_image_ratio(load_image('buttons/play.png'), self.button_size)
        self.about_button = scale_image_ratio(load_image('buttons/about.png'), self.button_size)

        self.player_img = load_image("player.png")

        # Fonts-----------------------------#
        self.button_font = Font('large_font.png', (255, 255, 255), 2)
        self.score_font = Font('small_font.png', (255, 255, 255), 5)
        self._score_font = Font('small_font.png', (255, 255, 0), 5)

        # Music-----------------------------#
        self.laser_shoot = load_sound('laser_shoot.wav')
        self.laser_shoot_miss = load_sound('laser_shoot_miss.wav')
        self.explosion = load_sound('explosion.wav')
        self.hurt = load_sound('hurt.wav')

        pygame.mixer.music.load('data/sounds/background.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)

        self.clock = Clock(30)
        self._game = True
        self.game_start = False

        # Buttons-----------------------------------#
        self.buttons = {
            "play": self.play_button,
            "about": self.about_button,
        }

        # Particles--------------------------------------------------------#
        load_particle_images('data/images/particles/')
        self.particles = []

        self.player_size = self.player_img.get_size()
        self.player = Player(self.size[0], self.size[1] - 50, *self.player_img.get_size(), self.player_img)

        # Enemies-------------------------#
        self.enemy_manager = EnemyManager(self.size, self.explosion, self.hurt)
        self.background_pos = 0

        self.bullet_manager = BulletManager(self.size, self.bullet)

        self.explosion_sound = False

        self.scores = {
            "Total Characters": [0, Font('small_font.png', (0, 255, 0), 5)],
            "Errors": [0, Font('small_font.png', (255, 0, 0), 5)],
            "WPM": [0, Font('small_font.png', (255, 255, 0), 5)],
            "Accuracy": [0, Font('small_font.png', (255, 0, 255), 5)],
        }

        self.start_time = pygame.time.get_ticks()
        self.end_time = False

    def reset_game(self):
        for value in self.scores.values():
            value[0] = 0

        self.enemy_manager = EnemyManager(self.size, self.explosion, self.hurt)
        self.bullet_manager = BulletManager(self.size, self.bullet)
        self.player = Player(self.size[0], self.size[1] - 50, *self.player_img.get_size(), self.player_img)

        self.start_time = pygame.time.get_ticks()


    def background_images(self, speed = 1):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.grid, (0, self.background_pos))
        self.screen.blit(self.grid, (0, self.background_pos - self.size[1]))
        self.screen.blit(self.gradient, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        self.background_pos += speed
        if self.background_pos >= self.size[1]:
            self.background_pos = 0

    def start_game_screen(self):
        game = True
        title = Font('large_font.png', (255, 0, 0), 10)
        _title = Font('large_font.png', (255, 255, 255), 10)

        x = (self.size[0] - title.get_width("Key War")) // 2
        y = 50

        diff = 30
        button_width = -diff
        for button in self.buttons.values():
            button_width += button.get_width()
            button_width += diff

        button_y = 550
        pressed = False
        score_diff = 10

        accuracy = 0 if self.scores["Errors"][0] == 0 else self.scores["Errors"][0] / self.scores["Total Characters"][0]

        self.scores["Accuracy"][0] = 100 - round(accuracy * 100, 2)

        if self.end_time:
            time_minutes = ((self.end_time - self.start_time) / 1000) / 60
            words_typed = self.scores["Total Characters"][0] / self.enemy_manager.word_counter
            self.scores["WPM"][0] = round(words_typed / time_minutes, 2)

            print(time_minutes, words_typed, self.scores["WPM"][0], self.enemy_manager.word_counter)

        while game:
            if pressed:
                if pressed == "play":
                    self.game_start = True
                    game = False
                else:
                    webbrowser.open("https://github.com/rohit-dewaliya")
                pressed = False

            mouse_pos = pygame.mouse.get_pos()

            self.background_images(5)

            _title.display_fonts_with_border(self.screen, "Key War", [x, y], 5, (10, 130, 230), 5)

            button_x = (self.size[0] - button_width) // 2
            for item, button in self.buttons.items():
                if (button_x < mouse_pos[0] < button_x + button.get_width() and button_y < mouse_pos[1] < button_y +
                        button.get_height()):
                    self.screen.blit(scale_image_size(button, button.get_width() + 10, button.get_height() + 10),
                                     [button_x - 5, button_y - 5])
                    if not pressed and pygame.event.get(pygame.MOUSEBUTTONDOWN):
                        pressed = item
                else:
                    self.screen.blit(button, [button_x, button_y])
                button_x += button.get_width()
                button_x += diff

            score_count = len(self.scores)
            score_y = ((self.size[1] - (score_count * self.score_font.image_height) - (score_count - 1) * score_diff )
                       // 2) + 70
            for key, value in self.scores.items():
                text = key + " : " + str(value[0])
                width = self.score_font.get_width(text)
                score_x = (self.size[0] - width) // 2
                value[1].display_fonts(self.screen, text, [score_x, score_y], 5)
                score_y += self.score_font.image_height + score_diff

            for event in pygame.event.get():
                if event.type == QUIT:
                    self._game = False
                    game = False

            pygame.display.update()
            self.clock.tick()
        self.reset_game()
        self.main()

    def main(self):
        while self._game:

            mouse_pos = pygame.mouse.get_pos()

            self.background_images()

            for i, particle in sorted(enumerate(self.particles), reverse=True):
                alive = particle.update(1)
                if not alive:
                    self.particles.pop(i)
                else:
                    particle.draw(self.screen, [0, 0])

            self.bullet_manager.display(self.screen)
            self.player.display(self.screen, mouse_pos)
            for _ in range(10):
                self.particles.append(Particle([self.player.x + random.randint(-2, 2),
                                           self.player.y + 5 + random.randint(0, 20)], 'p',
                                           [random.randint(-1, 1), 5], 0.5, 0, random.choice([(255, 0, 0), (255, 255,
                                                                                                            0)]), True))

            self.enemy_manager.display_enemies(self.screen, self.particles)

            if self.enemy_manager.calculae_defeat():
                self.player.life -= 1

            self.player.display_life(self.screen)

            if self.player.life == 0:
                self.end_time = pygame.time.get_ticks()
                self.game_start = False

            if not self.game_start:
                self.start_game_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._game = False

                if event.type == pygame.KEYDOWN:
                    self.player.pressed_key = event.unicode
                    self.scores["Total Characters"][0] += 1
                    if self.enemy_manager.check_word_locked(self.player.pressed_key):
                        self.bullet_manager.add_bullet(self.player.x, self.player.y, self.enemy_manager.locked_enemy)
                        self.laser_shoot.play()
                    else:
                        self.scores["Errors"][0] += 1
                        self.laser_shoot_miss.play()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pass

            pygame.display.update()
            self.clock.tick()


if __name__ == "__main__":
    size = [600, 700]
    Enemy.screen_size = size
    game = Game(size)
    game.start_game_screen()
