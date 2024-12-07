#for this we need to install opencv-python
import cv2
import sys,os
import pygame
from pygame import *
import main1 as m1

video=cv2.VideoCapture(r"E:\SAI PRADYUMNA\Castle Defender\Intro_Video\Castle Defender.mp4")

while(video.isOpened()):
    ret,frame=video.read()
    frame=cv2.resize(frame,(1200,700))
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


