import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random


import main1 as m


def func2(castle,theme):

    pygame.init()

    W,H=1346,708
    WIN=pygame.display.set_mode((W,H))
    FPS=100
    clock=pygame.time.Clock()

    image = pygame.image.load(r"E:\MAIN_INTERFACE\CastleDefender\Enemy_Selection_With_Titles.png")
    scaled_image=pygame.transform.scale(image,(1346,708))


    click_here = pygame.image.load(r"E:\MAIN_INTERFACE\CastleDefender\bg\click_here.jpg")
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
            self.rect.centerx=230
            self.rect.centery=685

    class Click2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = scaled_click_here
            self.image.set_colorkey("WHITE")
            self.rect=self.image.get_rect()
            self.rect.centerx=520
            self.rect.centery=685

    class Click3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = scaled_click_here
            self.image.set_colorkey("WHITE")
            self.rect=self.image.get_rect()
            self.rect.centerx=810
            self.rect.centery=685

    class Click4(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = scaled_click_here
            self.image.set_colorkey("WHITE")
            self.rect=self.image.get_rect()
            self.rect.centerx=1110
            self.rect.centery=685

    class Click5(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = scaled_click_here
            self.image.set_colorkey("WHITE")
            self.rect=self.image.get_rect()
            self.rect.centerx=1260
            self.rect.centery=685
            
    click1=Click1()
    all_sprites.add(click1)
    click2=Click2()
    all_sprites.add(click2)
    click3=Click3()
    all_sprites.add(click3)
    click4=Click4()
    all_sprites.add(click4)
    click5=Click5()
    all_sprites.add(click5)


    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONUP:
                pos=event.pos
                if click1.rect.collidepoint(pos):
                    m.func1(0,castle,theme)
    
                elif click2.rect.collidepoint(pos):
                    m.func1(1,castle,theme)
               
                elif click3.rect.collidepoint(pos):
                    m.func1(2,castle,theme)
                 
                elif click4.rect.collidepoint(pos):
                    m.func1(3,castle,theme)
    
                elif click5.rect.collidepoint(pos):
                    m.func1(4,castle,theme)

        all_sprites.update()    
        draw() 
        all_sprites.draw(WIN)
        pygame.display.flip()
