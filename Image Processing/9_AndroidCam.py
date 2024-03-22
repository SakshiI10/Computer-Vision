# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:41:09 2024

@author: SMI
"""
#How to use android device camera as webcam in OPencv.

import cv2

camera = "http://192.168.253.160:8080/video"
#connect your laptop and android device with same network either wifi or hotspot

#Here parameter 0 is a path of any video use for webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
  
cap.open(camera)
print("check",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\vdo.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        #gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
