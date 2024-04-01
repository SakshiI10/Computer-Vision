# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:50:57 2024

@author: SMI
"""
# Task 1: Input image from user, convert it to Grayscale and store it.
import cv2

path="D:\\My codes\\Computer Vision\\Image Processing\\Resources\\a.jpg"
print("Entered path is: ",path)

img=cv2.imread(path,0)
img=cv2.resize(img,(500,500))
cv2.imshow("Converted Image",img)

var=cv2.waitKey(0)
if var==ord("q"):
    #it accept name of image and data
    cv2.imwrite("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Output.png",img)
else:
    cv2.destroyAllWindows()
    