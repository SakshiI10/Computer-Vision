# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:04:16 2024

@author: SMI
"""
#Threholding is a segmentation techique which is use to separate selected object from an image.
'''
Image Thresholding - If pixel value is greater than a threshold value, it is done on a gray scale image.
#Thresholding is of 3 type -  Simple thresholding, Adaptive thresholding, Otsu’s thresholding
#simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)
#it return 2 values - one is random data , second is threshold
'''
import cv2 

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\black_white.png",0)
img = cv2.resize(img,(300,300))
cv2.imshow("data",img)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("1 - THRESH_BINARY",th1)
cv2.imshow("2 -THRESH_BINARY_INV ", th2)
cv2.imshow("3- THRESH_TRUNC", th3)
cv2.imshow("4 - THRESH_TOZERO", th4)
cv2.imshow("5 - THRESH_TOZERO_INV", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()