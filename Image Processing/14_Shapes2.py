# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:49:27 2024

@author: SMI
"""
import numpy as np
import cv2

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\thor.jpg")
img = cv2.resize(img,(600,700))

#create window of black screen
#img = np.zeros([512, 512, 3], np.uint8)*255  

#create window of white screen
img = np.ones([512,512,3], np.uint8)*255 

#Here line accept 5 parameter (img, starting, ending, color, thickness)
img = cv2.line(img, (0,0), (200,200), (254, 7, 31), 8) #color format BGR 

#arrowed line accept also accpet 5 parameter (img, starting, ending, color, thickness) 
img = cv2.arrowedLine(img, (0,125), (255,255), (255, 0, 125), 10)

#Rectangle - accept parameter(img, start_co, end_co, color code, thickness)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)

#circle - accept(img, centre, radius, color, thickness)
img = cv2.circle(img, (447, 125), 63, (214, 255, 0), -5)

font = cv2.FONT_ITALIC
#puttext -accept(img, text, start_co, font, fontsize, color, thickness, linetype)
img = cv2.putText(img, 'SMI', (20, 500), font, 4, (0, 125, 255), 10,cv2.LINE_AA)

#ellipse-accept(img, start_cor, (length,height), color, thickness)
img = cv2.ellipse(img,(400,600),(100,50),0,0,180,155,5)

#pts = np.array([[100,150],[200,30],[170,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#img = cv2.polylines(img,[pts],True,(0,255,155))

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 