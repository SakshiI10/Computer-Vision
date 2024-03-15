# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:30:25 2024

@author: SMI
"""

#HSV -  Hue saturation value
#Hsv is use to separate image information on the basis of color luminous or intensity.
#We use Hsv where we perform operation on the basis of color.
#HSV related to hexagon color model

# Hue is used to select color from 360 portion 
# Staturation is amount of color  which is selected in hue.(color shades)
# Valueis brightness of the color.

import cv2
import numpy as np

frame = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\color_balls.jpg")
while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_v = np.array([110,50,50])
    u_v = np.array([130,235,225])
    
    #Creating Mask
    mask = cv2.inRange(hsv, l_v, u_v)
    #filter mask with image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()







