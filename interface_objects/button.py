import pygame
import typing

from .patch import Patch


class Button(Patch):
    _callback: typing.Callable[[], None]

    def __init__(self, callback, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._callback = callback

    def process_click(self, event):
        if event.pos[0] < self.position[0] or event.pos[0] > self.position[0] + self.size[0]:
            return
        if event.pos[1] < self.position[1] or event.pos[1] > self.position[1] + self.size[1]:
            return
        self._callback()