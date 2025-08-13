import pygame

from .colorful_element import ColorfulElement


class Label(ColorfulElement):
    _text: str
    _font_size: int

    def __init__(self, position: tuple[int, int], size: tuple[int, int], text: str = "", color: tuple[int, int, int] = tuple([255, 0, 0]), font_size: int = 30):
        super().__init__(position, size)

        self._render = None

        self._font_size = font_size
        self._font = pygame.font.Font(None, font_size)

        self._text = ""
        self.text = text


    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    def draw(self, screen):
        self._render = self._font.render(self.text, 1, self.color)
        screen.blit(self._render, self._position)