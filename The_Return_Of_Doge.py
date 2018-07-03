import sys
import pygame
import random
from pygame.locals import *

width = 1280
height = 720

def update():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def draw(window):
    passwindow = pygame.display.set_mode((width, height))
    pygame.display.update()

def Game_Start():
    pygame.init()
    window = pygame.display.set_mode((width, height))
    window.fill((0,0,0))
    while True:
        update()
        draw(window)

if __name__ == '__main__':
    Game_Start()
