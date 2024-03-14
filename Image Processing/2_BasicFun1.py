# -*- coding: utf-8 -*-
"""
2.
@author: SMI
"""
#openCV use as cv2 in python
import cv2

#this function is used to read the image from location
img=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",1)
print(img)
#this function is used to resize the image
img=cv2.resize(img,(700,700))
#it accept 3 parameters 0,-1,1
img=cv2.flip(img,0)
print(img)

#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img2=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",1)
print(img2)
img2=cv2.resize(img2,(700,700))
print(img2)

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img3=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",0)
print(img3)
img3=cv2.resize(img3,(700,700))
print(img3)

cv2.imshow("Original Image",img)
cv2.imshow("More Saturated Image",img2)
cv2.imshow("Gray Image",img3)

#here parameter inside waitkey handle the life duration of an image
cv2.waitKey()
cv2.destroyAllWindows()