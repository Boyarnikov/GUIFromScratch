import pygame
import random


class InterfaceElement:
    _position: tuple[int, int]
    _size: tuple[int, int]

    def __init__(self, position: tuple[int, int], size: tuple[int, int]):
        self._position = position
        self._size = size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: tuple[int, int]):
        self._position = position

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: tuple[int, int]):
        self._size = size

    def draw(self, screen):
        pass

    def update(self):
        pass

    def process_click(self, event):
        pass