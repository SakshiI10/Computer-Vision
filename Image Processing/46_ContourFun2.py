# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:16:53 2024

@author: SMI
"""
import cv2
import numpy as np

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Shapes.png")
img = cv2.resize(img,(500,500))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,240,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour",cnts,"\ntotal contour",len(cnts))
#print("Hierarchy==\n",hier)
   
cv2.imshow("original",img)
cv2.imshow("gray",img1)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
