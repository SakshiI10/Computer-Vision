# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:12:28 2024

@author: SMI
"""
import cv2
import numpy as np

#load image into gray scale
img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\building.jpg")
img = cv2.resize(img,(300,300))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')
    
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
