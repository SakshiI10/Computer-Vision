# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:44:44 2024

@author: SMI
"""
import cv2
import numpy as np

img=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\roi_opr.jpg")
img=cv2.resize(img,(800,800))

#now pass like [y1:y2,x1:x2]
roi = img[55:210,320:440]
#cv2.imshow("roi image",roi)

#putting roi into any pixel values
img[50:205,431:551] = roi  
img[50:205,552:672] = roi 
img[50:205,200:320] = roi
img[50:205,80:200] = roi

#changing y
img[400:555,60:180] = roi

#Now try to use one image data into another image
img1 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\ironman.jpg")
img1 = cv2.resize(img1,(900,600))
img1[1:156,560:680] = roi

cv2.imshow("Image 1",img)
cv2.imshow("Image 2",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()