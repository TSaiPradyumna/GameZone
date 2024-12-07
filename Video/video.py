import numpy as np
import cv2

video=cv2.VideoCapture(r"E:\SAI PRADYUMNA\Castle Defender\Intro_Video\Castle Defender.mp4")
video.set(3,500)
video.set(4,500)

while (True):
    ret,frame=video.read()
    cv2.imshow("output",frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

video.release()
cv2.destroyAllWindows()