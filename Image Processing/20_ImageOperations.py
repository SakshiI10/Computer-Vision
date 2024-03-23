# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:21:22 2024

@author: SMI
"""
import cv2
import numpy as np

img=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\pikachu.jpg")
img = cv2.resize(img,(300,300))

#returns a tuple of number of rows, columns, and channels
print("shape",img.shape) 

#returns Total number of pixels is accessed
print("no.of pixels",img.size) 

#returns Image datatype is obtained
print("datatype",img.dtype) 

print("Imagetype",type(img))
#cv2.imshow("res",img)

#split  -  return 3 channel of ur image which is blue,green,red
print(cv2.split(img))
b,g,r = cv2.split(img)
'''
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("Original",img)'''

#To mix the the channels then use merge
cv2.imshow("Original",img)
mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

mr2 = cv2.merge((g,b,r))
cv2.imshow("gbr",mr2)

mr2 = cv2.merge((b,g,r))
cv2.imshow("bgr",mr2)

cv2.waitKey()
cv2.destroyAllWindows()