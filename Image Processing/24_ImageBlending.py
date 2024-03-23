# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:49:02 2024

@author: SMI
"""
#Image Blending with open cv 

#Here We use two important functions cv2.add(), cv2.addWeighted().
#Blending means addition of two images, if you want to blend two images then both have same size
import cv2
import numpy as np

#read two different images of same channel
img1 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\thor.jpg")
img2 = cv2.resize(img2,(500,700))
cv2.imshow("Thor",img1)
cv2.imshow("Bro Thor",img2)

#Now perform blending
#numpy addition in this we get module between value
result = img2+img1  
#cv2.imshow("Result", result)

#recommended to use cv2.add
#its your saturated operation which means value to value
result1 = cv2.add(img1,img2) 
#cv2.imshow("Result 1", result1)

#sum of both the weight = w1 + w2 = 1(max)
#function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)
result2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("Result 2",result2)

cv2.waitKey(0)
cv2.destroyAllWindows()