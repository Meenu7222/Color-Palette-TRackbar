# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:22:58 2023

@author: HP
"""

import cv2
import numpy as np
def emp():
    pass
img=np.zeros((512,512,3),np.uint8)
W="open cv color palete"
cv2.namedWindow(W)
cv2.createTrackbar('blue',W,0,255,emp)
cv2.createTrackbar('green',W,0,255,emp)
cv2.createTrackbar('red',W,0,255,emp)
while True:
    cv2.imshow(W,img)
    if cv2.waitKey(1) == 21:
        break
    blue=cv2.getTrackbarPos('blue',W)
    green=cv2.getTrackbarPos('green',W)
    red=cv2.getTrackbarPos('red',W)
    img[:]=[blue,green,red]
    print(blue,green,red)
cv2.destroyAllWindows()    
