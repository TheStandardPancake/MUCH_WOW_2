import sys
import pygame
import math
from time import sleep
from pygame.locals import *

#initialising pygame
pygame.init()

#setting the window measurements
width = 1280
height = 720

#Loading in the awesome Music
background_music = pygame.mixer.music.load("Wake Me Up Inside- Kazoo Cover.wav")
class spurt(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(window, self.color, (self.x,self.y), self.radius-1)

    @staticmethod
    def spurtpath(startx, starty, power, angle, time):
        pass


class doritos_pile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("doritos_pile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 75
        self.rect.y = 420

    def display(self):
        global window
        window.blit(self.image, self.rect)

    def elmo_reached_stash(self):
        if pygame.sprite.collide_mask(MLG_elmo, doritos_pile):
            Game_Over()

class the_doge(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("doge.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 335
        self.rect.y = 520

    def display(self):
        global window
        window.blit(self.image, self.rect)

class play_button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('start_button.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = width/2-self.rect.width/2
        self.rect.y = height/2-self.rect.height/2

    def display(self):
        global window
        window.blit(self.image, self.rect)

    def sensing_click(self):
        x,y = pygame.mouse.get_pos()
        if x >= width/2-self.rect.width/2 and x <= width/2+self.rect.width/2:
            Mouse_Location_X = True
        if x < width/2-self.rect.width/2 or x > width/2+self.rect.width/2:
            Mouse_Location_X = False
        if y >= height/2-self.rect.height/2 and y <= height/2+self.rect.height/2:
            Mouse_Location_Y = True
        if y < height/2-self.rect.height/2 or y > height/2+self.rect.height/2:
            Mouse_Location_Y = False
        if Mouse_Location_X == True and Mouse_Location_Y == True:
            self.image = pygame.image.load('start_button2.png').convert_alpha()
        else:
            self.image = pygame.image.load('start_button.png').convert_alpha()
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            entry_load()

def entry_load():
    #loading in all the slides for the animation + the new background and stuff
    level_layout = pygame.image.load('background.png').convert_alpha()
    slide_1 = pygame.image.load("title1.png").convert_alpha()
    slide_2 = pygame.image.load("title2.png").convert_alpha()
    slide_3 = pygame.image.load("title3.png").convert_alpha()
    slide_4 = pygame.image.load("title4.png").convert_alpha()
    slide_5 = pygame.image.load("title5.png").convert_alpha()
    slide_6 = pygame.image.load("title6.png").convert_alpha()
    slide_7 = pygame.image.load("title7.png").convert_alpha()
    slide_8 = pygame.image.load("title8.png").convert_alpha()
    slide_9 = pygame.image.load("title9.png").convert_alpha()
    slide_10 = pygame.image.load("title10.png").convert_alpha()
    global doritos_pile
    doritos_pile = doritos_pile()
    global Doge
    Doge = the_doge()
    #blitting them in an animation
    global window
    window.blit(level_layout, (0,0))
    window.blit(slide_1, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    window.blit(slide_2, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    window.blit(slide_3, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    window.blit(slide_4, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    window.blit(slide_5, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    window.blit(slide_6, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    window.blit(slide_7, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    window.blit(slide_8, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    window.blit(slide_9, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    window.blit(slide_10, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    Game_Start()


def update(): #So far this just lets you exit the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def Title_screen(): #Just a title screen, as the name suggests
    pygame.mixer.music.play(-1)
    #load title screen
    global window
    window = pygame.display.set_mode((width, height))
    heading = pygame.image.load('proper_title.png').convert_alpha()
    curtains = pygame.image.load('the_initial_title_screen.png').convert_alpha()
    pygame.display.set_caption("Elmo's Revenge")
    # Drawing the title screen
    while True:
        window.blit(curtains, (0, 0))
        window.blit(heading, (480,25))
        startbutton = play_button()
        startbutton.sensing_click()
        startbutton.display()
        update()
        pygame.display.update()

def re_draw():
    window.blit(level_layout, (0,0))
    Doge.display()
    doritos_pile.display()
    pygame.draw.line(window, (0,0,0), line[0], line[1])
    mountaindew.draw(window)

    pygame.display.update()

def Game_Start():
    global level_layout
    level_layout = pygame.image.load('background.png').convert_alpha()
    global mountaindew
    mountaindew = spurt(300, 494,  5, (34,245,34))
    global line
    global pos

    while True:
        pos = pygame.mouse.get_pos()
        line = [(mountaindew.x, mountaindew.y), pos]
        re_draw()
        update()

def Game_over():
    quit()

if __name__ == '__main__':
    Title_screen()
