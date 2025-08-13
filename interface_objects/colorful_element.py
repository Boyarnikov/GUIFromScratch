import pygame
import random


from .interface_element import InterfaceElement


class ColorfulElement(InterfaceElement):
    _position: tuple[int, int]
    _size: tuple[int, int]

    def __init__(self, position: tuple[int, int], size: tuple[int, int], color: tuple[int, int, int] = tuple([255, 0, 0])):
        super().__init__(position, size)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: tuple[int, int, int]):
        self._color = color