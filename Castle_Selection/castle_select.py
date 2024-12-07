import pygame,sys
from pygame import *
from pygame import mixer
import time
import os
import random
pygame.init()

W,H=500,500
WIN=pygame.display.set_mode((W,H))
FPS=100
clock=pygame.time.Clock()   

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
