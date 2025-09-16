import pygame
import math

from data.scripts.image_functions import load_image, swap_color, scale_image_ratio, clip_surface

class Font():
    def __init__(self, path, color = (255, 0, 0), size_ratio = 1):
        self.size_ratio = size_ratio
        self.image = load_image('fonts/' + path)
        self.image = swap_color(self.image, (255, 0, 0), color)
        self.image_size = [self.image.get_width(), self.image.get_height()]
        self.image = scale_image_ratio(self.image, size_ratio)
        self.image_height = self.image.get_height()
        self.character_size = {}
        self.image_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', '-', ',', ':', '+', "'", '!', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '/', '_', '=', '\\', '[', ']', '*', '"', '<', '>', ';', ' ']
        self.image_character_dict = {}
        self.image_character = 0
        self.image_x = 0
        self.image_x_size = 0

        for pixel in range(0, self.image.get_width()):
            pixel_color = self.image.get_at((pixel, 0))

            if pixel_color == (127, 127, 127):
                if self.image_x_size == 0:
                    continue
                self.image_character_dict[self.image_characters[self.image_character]] = [clip_surface(self.image, pixel - self.image_x_size, 0, self.image_x_size, self.image_height), self.image_x_size]
                self.character_size[self.image_characters[self.image_character]] = self.image_x_size
                self.image_x_size = 0
                self.image_character += 1
                continue
            else:
                self.image_x_size += 1

    def get_width(self, string, text_spacing=3):
        width = 0
        _len = len(string)

        for i in range(0, _len):
            character = string[i]
            if character == ' ':
                width += 5 * self.size_ratio
            else:
                space = text_spacing if i < _len - 1 else 0
                width += self.image_character_dict[character][1] + space

        return width

    def display_fonts(self, surface, string, pos, text_spacing = 3, alpha = 255):
        for character in string:
            if character == ' ':
                pos[0] += 5 * self.size_ratio
            else:
                char_img = self.image_character_dict[character][0].copy()
                char_img.set_alpha(alpha)
                surface.blit(char_img, pos)
                pos[0] += self.image_character_dict[character][1] + text_spacing

    def display_fonts_with_border(self, surface, string, pos, text_spacing=3, border_color=(0, 0, 0), border_size=1,
                                  alpha = 255):
        base_x, base_y = pos[0], pos[1]

        for dx in range(-border_size, border_size + 1):
            for dy in range(-border_size, border_size + 1):
                if dx == 0 and dy == 0:
                    continue
                offset_pos = [base_x + dx, base_y + dy]
                self._draw_string(surface, string, offset_pos, text_spacing, color_override=border_color)

        # Draw main text on top
        self.display_fonts(surface, string, [base_x, base_y], text_spacing, alpha)

    def _draw_string(self, surface, string, pos, text_spacing, color_override=None):
        for character in string:
            if character == ' ':
                pos[0] += 5 * self.size_ratio
            else:
                char_img = self.image_character_dict[character][0]
                if color_override:
                    char_img = char_img.copy()
                    char_img.fill(color_override + (255,), special_flags=pygame.BLEND_RGBA_MIN)

                surface.blit(char_img, pos)
                pos[0] += self.image_character_dict[character][1] + text_spacing

    @staticmethod
    def render_water_text(font_surface, time, amplitude=5, wavelength=50, speed=10):
        w, h = font_surface.get_size()
        distorted = pygame.Surface((w, h), pygame.SRCALPHA)

        for y in range(h):
            offset_x = int(math.sin((y / wavelength) + time * speed) * amplitude)
            row = font_surface.subsurface((0, y, w, 1))
            distorted.blit(row, (offset_x, y))

        return distorted