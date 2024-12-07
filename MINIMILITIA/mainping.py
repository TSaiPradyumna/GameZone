import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random
pygame.init()

W,H=394,448
WIN=pygame.display.set_mode((W,H))
FPS=100
clock=pygame.time.Clock()   


image3 = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\0 - Copy.jpg")
scaled_image3=pygame.transform.scale(image3,(500,500))

player_image = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\fi1.jpg")
scaled_player_image=pygame.transform.scale(player_image,(30,30))
rotated_right_player_image1=pygame.transform.rotate(scaled_player_image,0)
image_rect1=scaled_player_image.get_rect()
r_image_rect1=rotated_right_player_image1.get_rect()

player_image2 = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\fi1.png")
scaled_player_image2=pygame.transform.scale(player_image2,(30,30))
image_rect2=scaled_player_image2.get_rect()


def draw():

        WIN.blit(scaled_image3, (0, 0))

class Player01(pygame.sprite.Sprite):
    def __init__(self):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = rotated_right_player_image1
        # self.image.set_colorkey("BLACK")
        self.rect=self.image.get_rect()
        self.rect.centerx=10
        self.rect.centery=448
        self.rect.bottom = 448
        self.speedy=0
        self.speedx =0




    def update(self):
        self.speedx=0
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
            self.image = scaled_player_image2
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
            self.image = rotated_right_player_image1
        if keystate[pygame.K_UP]:
            self.speedy=-5
            # self.image =rotated_up_player_image1
        if keystate[pygame.K_DOWN]:
            self.speedy=5
            # self.image = rotated_down_player_image1
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>394:
            self.rect.right=394
        if self.rect.bottom>448:
            self.rect.bottom=448
        if self.rect.top<0:
            self.rect.top=0
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy

all_sprites=pygame.sprite.Group()
player01=Player01()
all_sprites.add(player01)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    all_sprites.update()

        
    draw()
    all_sprites.draw(WIN)
    pygame.display.update()
