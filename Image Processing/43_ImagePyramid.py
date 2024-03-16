# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 22:27:23 2024

@author: SMI
"""
#Image Pyramids in OpenCV; It is used to create images of different resolutions and to use these pyramids to blends the images.
#There are two types of Image Pyramid-
# 1) Gaussian Pyramid and 2) Laplacian Pyramids
import cv2

#load image into gray scale
img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\thor.jpg")
img = cv2.resize(img,(700,700))

#Gaussian Pyramid Have 2 function-1) cv2.pyrUp(),2)-cv2.pyrDown()
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)
pu1 = cv2.pyrUp(pd2)
'''
cv2.imshow("original",img)
cv2.imshow("pd1",pd1)
cv2.imshow("pd2",pd2)
cv2.imshow("pu1",pu1)
'''

img1 = img.copy()
data = [img1]
for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
