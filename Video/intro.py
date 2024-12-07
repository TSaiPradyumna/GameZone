from Video.pyvidplayer import Video

#Video Initiation
vid=Video(r"E:\SAI PRADYUMNA\Castle Defender\Intro_Video\Castle Defender.mp4")
vid.set_size((1346,708))

import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random
pygame.init()

W,H=1364,708
win=pygame.display.set_mode((W,H))
FPS=100
clock=pygame.time.Clock()   



def intro():
    while True:
        vid.draw(win,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_game()

def main_game():
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
intro()

