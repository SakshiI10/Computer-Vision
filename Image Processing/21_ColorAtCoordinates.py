# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:36:43 2024

@author: SMI
"""
import cv2

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\lion.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("lion",img)

#access a pixel value by its row and column coordinates.
px = img[520,580] #store cordinate in variable
print("The pixel of that co-ordinates: ",px) #we get the pixel value

#Now try to find selected channel value from cordinate
#We know we have three channel -   0,1,2
# accessing only blue pixel
blue = img[520,580,0]
print("the pixel having blue color: ",blue)

grn = img[520,580,1] #for green pass 1
print("the pixel having grn color: ",grn)

red = img[520,580,2] #for red pass 2
print("the pixel having red color: ",red)

cv2.waitKey(0)
cv2.destroyAllWindows()