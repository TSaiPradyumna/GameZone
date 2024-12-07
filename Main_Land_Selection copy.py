import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random

import Main_Castle_Selection as CastleSelect1


pygame.init()

W,H=1346,708
WIN=pygame.display.set_mode((W,H))
FPS=100
clock=pygame.time.Clock()

image = pygame.image.load(r"D:\Castle Defender\Theme_Selection_with_titles.png")
scaled_image=pygame.transform.scale(image,(1346,708))


click_here = pygame.image.load(r"D:\Castle Defender\bg\click_here.jpg")
scaled_click_here=pygame.transform.scale(click_here,(45,45))


def draw():
        WIN.blit(scaled_image, (0, 0))

all_sprites=pygame.sprite.Group()


class Click1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_click_here
        self.image.set_colorkey("WHITE")
        self.rect=self.image.get_rect()
        self.rect.centerx=540
        self.rect.centery=290

class Click2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_click_here
        self.image.set_colorkey("WHITE")
        self.rect=self.image.get_rect()
        self.rect.centerx=1000
        self.rect.centery=290

class Click3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_click_here
        self.image.set_colorkey("WHITE")
        self.rect=self.image.get_rect()
        self.rect.centerx=540
        self.rect.centery=565

class Click4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_click_here
        self.image.set_colorkey("WHITE")
        self.rect=self.image.get_rect()
        self.rect.centerx=1015
        self.rect.centery=565
        
click1=Click1()
all_sprites.add(click1)
click2=Click2()
all_sprites.add(click2)
click3=Click3()
all_sprites.add(click3)
click4=Click4()
all_sprites.add(click4)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONUP:
            pos=event.pos
            if click1.rect.collidepoint(pos):
                os.system(r"D:\Castle Defender\main1.py")
                CastleSelect1.func1()
            elif click2.rect.collidepoint(pos):
                os.system(r"D:\Castle Defender\main2.py")
                CastleSelect1.func1()
            elif click3.rect.collidepoint(pos):
                os.system(r"D:\Castle Defender\main3.py")
                CastleSelect1.func1()
            elif click4.rect.collidepoint(pos):
                os.system(r"D:\Castle Defender\main4.py")
                CastleSelect1.func1()
    all_sprites.update()    
    draw() 
    all_sprites.draw(WIN)
    pygame.display.flip()
