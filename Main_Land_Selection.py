import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random
from pygame import mixer
import Main_Castle_Selection as MSC


pygame.init()
mixer.init()


W,H=1346,708
WIN=pygame.display.set_mode((W,H))
FPS=100
clock=pygame.time.Clock()

image = pygame.image.load(r"E:\MAIN_INTERFACE\CastleDefender\Theme_Selection_with_titles.png")
scaled_image=pygame.transform.scale(image,(1346,708))


click_here = pygame.image.load(r"E:\MAIN_INTERFACE\CastleDefender\bg\click_here.jpg")
scaled_click_here=pygame.transform.scale(click_here,(45,45))

mixer.music.load(r"E:\MAIN_INTERFACE\CastleDefender\Background_Music\house_lo.mp3")
mixer.music.play(-1)
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
                MSC.func1(0)
            elif click2.rect.collidepoint(pos):
                MSC.func1(1)
            elif click3.rect.collidepoint(pos):
                MSC.func1(2)
            elif click4.rect.collidepoint(pos):
                MSC.func1(3)
    all_sprites.update()    
    draw() 
    all_sprites.draw(WIN)
    pygame.display.flip()



