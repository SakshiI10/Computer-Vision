# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 13:27:06 2024

@author: SMI
"""
'''
GrabCut Algoritm can cutoff any foreground object from image or video.
It works like a rectangle portion mark on the image and area outise the rectangle is treated as an extra part and removes it completely.
Gaussian mixtuere model help to achieve the target.
'''
import	numpy  as  np
import	cv2

img  =	cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\car.jpg")
img = cv2.resize(img,(800,800))
mask =	np.zeros(img.shape[:2],np.uint8)
 
bgdModel =  np.zeros((1,65),np.float64)*255
fgdModel =  np.zeros((1,65),np.float64)*255
 
#parameter(img,mask,rect,bgmodel,fgmodel,iter,method) 
rect =	(134,150,660,730)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5, cv2.GC_INIT_WITH_RECT)
 
mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
img  =	img*mask2[:,:,np.newaxis]
 
cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()