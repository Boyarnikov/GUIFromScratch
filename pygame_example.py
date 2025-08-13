import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        pass

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)
