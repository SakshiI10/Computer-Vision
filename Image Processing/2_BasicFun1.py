# -*- coding: utf-8 -*-
"""
2.
@author: SMI
"""
import cv2

img=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",1)
print(img)
img=cv2.resize(img,(700,700))
img=cv2.flip(img,0)
print(img)

img2=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",1)
print(img2)
img2=cv2.resize(img2,(700,700))
print(img2)

img3=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Nature.jpg",0)
print(img3)
img3=cv2.resize(img3,(700,700))
print(img3)

cv2.imshow("Original Image",img)
cv2.imshow("More Saturated Image",img2)
cv2.imshow("Gray Image",img3)
cv2.waitKey()
cv2.destroyAllWindows()