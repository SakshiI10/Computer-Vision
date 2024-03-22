# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:31:18 2024

@author: SMI
"""
import cv2

cap = cv2.VideoCapture(0)
print(cap)

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
  
#It contain 4 parameter: name, codec,fps,resolution
output = cv2.VideoWriter("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\output.avi",fourcc,20.0,(640,480))

while(cap.isOpened()):
    #here read the vdo
    ret, vdo = cap.read()  
    
    if ret==True:
        gray  = cv2.cvtColor(vdo,cv2.COLOR_BGR2GRAY)
        #here flip is used to flip the video at recording time
        vdo = cv2.flip(vdo,1)
        gray = cv2.flip(gray,1)
        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',vdo)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
cap.release()
cv2.destroyAllWindows()