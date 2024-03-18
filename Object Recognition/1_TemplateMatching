# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:52:50 2024

@author: SMI
"""
"""
Template Matching: It is a method for searching and finding the location of a template image in a larger image.
OpenCV comes with a function cv2.matchTemplate() for this purpose. 
It simply slides the template image over the input image(as in 2D convolution) and compares the template and patch of input image under the template image. 
"""
import cv2
import numpy as np

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\avengers.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\temp.jpg", 0)
w, h = template.shape[::-1]

#this function accept prameters (img,template,method)
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED)
print("Result",res)

threshold = 0.999
loc = np.where(res >= threshold)  #find brightest point
print("Bright pixels",loc)
count = 0
for i in zip(*loc[::-1]):
    print("i",i)
    cv2.rectangle(img, i, (i[0] + w, i[1] + h), (0, 0, 255), 2)
    count+=1
print("Number of iterations",count)

img = cv2.resize(img,(400,400))
res = cv2.resize(res,(400,400))

cv2.imshow("Img", img)
cv2.imshow("Match temp",res)

cv2.waitKey(0)
cv2.destroyAllWindows()
