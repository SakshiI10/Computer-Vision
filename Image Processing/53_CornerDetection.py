# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:00:38 2024

@author: SMI
"""
#Feature Detection and Description.
#Harris Corner Detection 
"""
OpenCV has the function cv2.cornerHarris() for this purpose. 
Its arguments are : img - Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection
ksize - Aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.
"""
import numpy as np
import cv2

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Shapes.png")
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
'''
res= cv.cornerHarris(gray, 2, 3, 0.04)
res = cv.dilate(res, None)
img[res > 0.01 * res.max()] = [0, 0, 255]  # marked color

cv.imshow('dst', img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
'''

#parameters (img,no.of corner,quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,100,0.01,20)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("res",img)

cv2.waitKey(0)
cv2.destroyAllWindows()