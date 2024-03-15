# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:43:25 2024

@author: SMI
"""
# Creating Image Border

import cv2

img=cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\lion.jpg")
img=cv2.resize(img,(500,500))

border=cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255,0,125])

cv2.imshow("Image",border)
cv2.waitKey(0)
cv2.destroyAllWindows()