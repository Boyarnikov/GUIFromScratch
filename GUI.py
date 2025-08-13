import pygame
import time
import random


class Clock:
    """Example of how internal clock can work (this one blocks input tho)"""

    def __init__(self, frame_rate=1):
        self._time = time.time()
        self.frame_rate = frame_rate

    def tick(self, frame_rate=None):
        frame_rate = frame_rate or self.frame_rate

        current_time = time.time()
        if current_time - self._time < 1 / frame_rate:
            time.sleep(1 / frame_rate - current_time + self._time)

        self._time = time.time()


class GUI:
    _instance = None
    _is_running = False

    _elements: list

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pygame.init()
        self._elements = []

        self._screen = pygame.display.set_mode((500, 500))
        self._clock = Clock(60)  # pygame.time.Clock()

    def _handle_drawing(self):
        self._screen.fill((255, 255, 255))

        for element in self._elements:
            element.draw(self._screen)

        pygame.display.flip()

    def _handle_update(self):
        for element in self._elements:
            element.update()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for element in self._elements:
                    element.process_click(event)

    def add_element(self, element):
        self._elements.append(element)

    def run(self):
        self._is_running = True

        while self._is_running:
            self._handle_input()
            self._handle_update()
            self._handle_drawing()

            self._clock.tick(60)

        pygame.quit()
