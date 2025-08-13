import pygame

from .colorful_element import ColorfulElement


class Patch(ColorfulElement):
    def draw(self, screen):
        pygame.draw.rect(screen, self._color, pygame.Rect(*self._position, *self._size))