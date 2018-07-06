import sys
import pygame
import math
import random
from time import sleep
from pygame.locals import *

#initialising pygame
pygame.init()

#setting the window measurements
width = 1280
height = 720

#Loading in the awesome Music
background_music = pygame.mixer.music.load("Wake Me Up Inside- Kazoo Cover.wav")

#making a class for the projectile
class dorito_projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dorito.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        global blip
        global blop
        blip = 0
        blop = 0

    def draw(self, window):
        self.rect.x = self.x
        self.rect.y = self.y
        window.blit(self.image, self.rect)

    def super(self):
        global blip
        global blop
        blip += 1
        if blip == 20:
            blop += 1
            blip = 0
        if blop % 2 == 0:
            self.image = pygame.image.load('super_dorito.png')
        else:
           self.image = pygame.image.load('dorito.png')

    @staticmethod
    def dorito_projectile_path(startx, starty, power, angle, time):
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distx = velx * time
        disty = (vely * time) + ((-9.6 * (time)**2)/2)

        newx = round(distx + startx)
        newy = round(starty - disty)

        return(newx, newy)

#making the doritos pile load in:
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

#making the elmo Sprite
class elmo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("elmo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 670-self.rect.height

    def display(self):
        global window
        global un_official_score
        global Doge
        if self.rect.x > Doge.rect.x:
            self.rect.x += random.choice([1,-1,-1,-1])*un_official_score
        if self.rect.x < Doge.rect.x:
            self.rect.x += 1*un_official_score
        if self.rect.y > Doge.rect.y:
            self.rect.y += random.choice([1,-1,-1])*un_official_score
        if self.rect.y < Doge.rect.y:
            self.rect.y += random.choice([1,1,-1])*un_official_score
        window.blit(self.image, self.rect)

    def collisions(self):
        if pygame.sprite.collide_mask(self, Doge):
            global playing
            playing = False
            pygame.mixer.music.stop()
            background_music = pygame.mixer.music.load("sad_violin.mp3")
            pygame.mixer.music.play(-1)
            ending_animation()
            game_over_screen()
        if pygame.sprite.collide_mask(self, dorito):
            global un_official_score
            un_official_score += 1
            self.rect.x = 1280
            self.rect.y = random.randrange(0,(670-self.rect.height))

class elmo_boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("boss_elmo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 720-self.rect.height
        self.hit_counter = 0
        self.alive = True
        self.music = True

    def display(self):
        global window
        self.rect.x -= 1
        window.blit(self.image, self.rect)
        while self.music == True:
            pygame.mixer.music.stop()
            background_music = pygame.mixer.music.load("Hello_Darkness.wav")
            pygame.mixer.music.play(-1)
            self.music = False

    def collisions(self):
        global panic_attack
        if pygame.sprite.collide_mask(self, Doge):
            global playing
            playing = False
            ending_animation()
            game_over_screen()
        if pygame.sprite.collide_mask(self, dorito) and panic_attack == False:
            self.hit_counter += 1
        elif pygame.sprite.collide_mask(self, dorito) and panic_attack == True:
            self.hit_counter += 50
        if self.hit_counter >= 5000:
            self.alive = False
            ending_animation()
            win_screen()

#panic button, for when the going gets tough
class panic_button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("panic_button.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50

    def display(self):
        global window
        window.blit(self.image, self.rect)

    def sensing_click(self):
        x,y = pygame.mouse.get_pos()
        if x >= self.rect.x and x <= self.rect.x+self.rect.width:
            Mouse_Location_X = True
        if x < self.rect.x or x > self.rect.x+self.rect.width:
            Mouse_Location_X = False
        if y >= self.rect.y and y <= self.rect.y+self.rect.height:
            Mouse_Location_Y = True
        if y < self.rect.y or y > self.rect.y+self.rect.height:
            Mouse_Location_Y = False
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            global panic_attack
            panic_attack = True

#making the doge Sprite
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

#the play button on title screen
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
            Game_Start()

class replay_button(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('replay.png').convert_alpha()
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
            self.image = pygame.image.load('replay2.png').convert_alpha()
        else:
            self.image = pygame.image.load('replay.png').convert_alpha()
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            entry_load()
            Game_Start()


#this is the curtains opening
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
    global doritospile
    global Doge
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
    doritospile.display()
    window.blit(slide_6, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritospile.display()
    window.blit(slide_7, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritospile.display()
    window.blit(slide_8, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritospile.display()
    window.blit(slide_9, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(level_layout, (0,0))
    Doge.display()
    doritospile.display()
    window.blit(slide_10, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)

#Thi is the ending animation of curtains closing
def ending_animation():
    blackness = pygame.image.load('black1.png').convert_alpha()
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
    #blitting them in an animation
    global window
    window.blit(blackness, (0,0))
    window.blit(slide_10, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_9, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_8, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_7, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_6, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_5, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_4, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_3, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_2, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)
    window.blit(blackness, (0,0))
    window.blit(slide_1, (0,0))
    update()
    pygame.display.update()
    sleep(0.1)

def update(): #So far this just lets you exit the game and makes everything work for unkown reasons
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
    global doritospile
    doritospile = doritos_pile()
    global Doge
    Doge = the_doge()
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
    pygame.draw.line(window, (0,0,0), line[0], line[1])
    window.blit(level_layout, (0,0))
    Doge.display()
    doritospile.display()
    if un_official_score <= 25:
        crawling_elmo.display()
    crawling_elmo.collisions()
    if un_official_score > 25 and boss_elmo.alive == True:
        panic.display()
        panic.sensing_click()
        boss_elmo.display()
    if panic_attack == True:
        dorito.super()
        dorito.draw(window)
    elif panic_attack == False:
        dorito.draw(window)
    boss_elmo.collisions()
    pygame.display.update()

#this is used to find the angle at which the projectile is launched
def findAngle(pos):
    sX = dorito.x
    sY = dorito.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle

#contains the main game loop
def Game_Start():
    global playing
    playing = True
    #dealing with music stuff
    pygame.mixer.music.stop()
    background_music = pygame.mixer.music.load("KazooSandstorm.wav")
    pygame.mixer.music.play(-1)

    #setting up the background image
    global level_layout
    level_layout = pygame.image.load('background.png').convert_alpha()

    #making the projectile + its variables
    global dorito
    dorito = dorito_projectile(402, 553)
    global line
    global pos
    x = 0
    y = 0
    time = 0
    power = 0
    angle = 0
    shoot = False

    #Making elmo enemy
    global crawling_elmo
    crawling_elmo = elmo()

    #the score system
    global un_official_score
    un_official_score = 1

    #Making boss_elmo
    global boss_elmo
    boss_elmo = elmo_boss()

    #panic Button
    global panic
    panic = panic_button()
    global panic_attack
    panic_attack = False

    while playing:
        if shoot:
            if dorito.y < 650 - dorito.rect.width/2 and dorito.x < 1280 and dorito.x > 0:
                time += 0.05
                po = dorito_projectile.dorito_projectile_path(x, y, power, angle, time)
                dorito.x = po[0]
                dorito.y = po[1]
            else:
                shoot = False
                dorito.y = 553
                dorito.x = 402
            if dorito.x > 1280 or dorito.x < 0:
                shoot = False
                dorito.y = 553
                dorito.x = 402
            if dorito.y > 720 or dorito.y < 0:
                shoot = False
                dorito.y = 553
                dorito.x = 402
            if pygame.sprite.collide_mask(dorito, crawling_elmo):
                shoot = False
                dorito.y = 553
                dorito.x = 402
            if pygame.sprite.collide_mask(dorito, boss_elmo):
                shoot = False
                dorito.y = 553
                dorito.x = 402

        pos = pygame.mouse.get_pos()
        line = [(dorito.x, dorito.y), pos]
        re_draw()
        update()
        if pygame.mouse.get_pressed()[0]:
            if shoot == False:
                shoot = True
                x = dorito.x
                y = dorito.y
                time = 0
                power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2)
                angle = findAngle(pos)


def game_over_screen():
    curtains = pygame.image.load('the_initial_title_screen.png').convert_alpha()
    replay = replay_button()
    while True:
        window.blit(curtains, (0, 0))
        replay.display()
        replay.sensing_click()
        update()
        pygame.display.update()

def win_screen():
    curtains = pygame.image.load('the_initial_title_screen.png').convert_alpha()
    win_banner = pygame.image.load("win_banner.png").convert_alpha()
    pygame.mixer.music.stop()
    background_music = pygame.mixer.music.load("kazoo_kid_trap_remix.wav")
    pygame.mixer.music.play(-1)
    while True:
        window.blit(curtains, (0, 0))
        window.blit(win_banner, (width/2, 150))
        update()
        pygame.display.update()


if __name__ == '__main__':
    Title_screen()
