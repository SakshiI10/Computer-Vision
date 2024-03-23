# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:01:56 2024

@author: SMI
"""
#result Blending with Trackbars 
import numpy as np
import cv2 
 
#read two different images of same channel
img1 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\roi_opr.jpg")
img1 = cv2.resize(img1,(500,700))

img2 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\thor.jpg")
img2 = cv2.resize(img2,(500,700))
    
def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)

#create track bar windows
cv2.namedWindow('Win') 

cv2.createTrackbar('TrackBar', 'Win', 1, 100, blend)

#create switch for invoke the trackbars
switch = '0 : OFF \n 1 : ON'  
#create track bar for switch
cv2.createTrackbar(switch, 'Win', 0, 1, blend)  

while True:
    a = cv2.getTrackbarPos('TrackBar','Win') 
    s = cv2.getTrackbarPos(switch,'Win')
    n = float(a/100)
    print(n)
    
    if s == 0:
        dst = img[:]
    else:
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst, str(a), (20, 50), cv2.FONT_ITALIC, 2, (0, 125, 255), 2)
    cv2.imshow('dst',dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.waitKey(0)    
cv2.destroyAllWindows()
