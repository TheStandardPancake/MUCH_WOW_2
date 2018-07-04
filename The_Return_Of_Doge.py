import sys
import pygame
import random
from pygame.locals import *

#initialising pygame
pygame.init()

#setting the window measurements
width = 1280
height = 720

class doritos_pile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("doritos_pile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 75
        self.rect.y = 420

    def elmo_reached_stash(self):
        if pygame.sprite.collide_mask(MLG_elmo, doritos_pile):
            Game_Over()

def update(): #So far this just lets you exit the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def Title_screen(): #Just a title screen, as the name suggests
    #Setting up the frames per second
    title = True
    #load title screen
    window = pygame.display.set_mode((width, height))
    heading = pygame.image.load('proper_title.png').convert_alpha()
    curtains = pygame.image.load('the_initial_title_screen.png').convert_alpha()
    pygame.display.set_caption("Elmo's Revenge")
    # Drawing the title screen
    while title:
        window.blit(curtains, (0, 0))
        window.blit(heading, (480,25))
        update()
        pygame.display.update()

def Game_Start():
    level_layout = pygame.image.load('background.png').convert_alpha()

    while True:
        update()

def Game_over():
    quit()

if __name__ == '__main__':
    Title_screen()
