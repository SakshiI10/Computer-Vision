# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:07:33 2024

@author: SMI
"""
#Canny Edge Detection using OpenCV
#Canny Edge Detection is a popular edge detection approach.
#It is a multi-stage algorithm to detect a edges.
#It was developed by John F. Canny in 1986.
#This approach combine with 5 steps.
# 1) - NOise reduction(gauss)),         2) - Gradient calculation
# 3) - Non-maximum suppresson,          4) - Double Threshold,
# 5) - Edge Tracking by Hysteresis 
import cv2
import numpy as np

#load image into gray scale
img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\building.jpg")
img = cv2.resize(img,(300,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#canny(img,thresh1,thres2)thresh 1 and thresh2 at different lvl
canny = cv2.Canny(img_gray,20,150)

cv2.imshow("original",img)
cv2.imshow("gray",img_gray)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
