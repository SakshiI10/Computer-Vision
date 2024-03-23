# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 21:35:43 2024

@author: SMI
"""
'''
#Image Smoothing or bluring are most common used operation in Image Processing. It is use to remove noise from the images. There are many filter  which is use for smoothing the image.
LOW Pass Filter(LPS): Use to remove Noise from the images.
High Pass Filter: Use to detect and finding edges in an image.
'''
import cv2
import numpy as np

img = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\noisy.jpg")  
img = cv2.resize(img,(400,400))
cv2.imshow("original",img)

#define a kernal for homogeneous function
kernel = np.ones((5,5),np.float32)/25

#FILTER NUMBER 1
#This filter works like each output pixel is the mean of its kernal neigbours
#It is homogeneous filter, where all pixel contribute with equal weight.
#kernal is a small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernal(h,w))*kernal]   
h_filter = cv2.filter2D(img,-1,kernel) # -1 is desired depth
cv2.imshow("homogeneous",h_filter)

#FILtER NUMBER 2
#Blur method or averaging
#It takes the avg of all the pixels under kernel area and 
#It replaces the central element with this average..
blur = cv2.blur(img,(8,8)) #here we have image and kernel as parameter
cv2.imshow("blur",blur)

#Filter Number 3------
#It uses different weight kernel,in  row as well as col.
#Means side values are small then centre .It manage distance b/w value of pixel.
gau= cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv2.imshow("gau blur",gau)
 
#Filter Number 4--
#Median Filter computes the median of all the pixels under the 
#Kernel window and the central pixel is replaced with this median value.
#This is highly effective in removing salt-and-pepper noise. 
#here kernal size must be odd except one
med = cv2.medianBlur(img,5)
cv2.imshow("median filter",med)

#bilateral filter is highly effective at noise removal while preserving edges.
#It work like gaussian filter but more focus on edges
#It is slow as compare with other filters
#Argument (img, neigbour_pixel_diameter,sigma_color,sigma_space)
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bi_f",bi_f)

#Now plot all the images on graph
titles = ["original_image","homo","blur","gauss","med","bi_f"]
images = [img,h_filter,blur,gau,med,bi_f]

#if you want then plot it
from matplotlib import pyplot as plt
for i in range(6):
    plt.subplot(2, 3, i+1), 
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
