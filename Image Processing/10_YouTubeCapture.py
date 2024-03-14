# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:55:45 2024

@author: SMI
"""
#Capture video from youtube

import cv2
import pafy

url = "https://www.youtube.com/watch?v=JPuenEXgp_M"
data=pafy.new(url)
data = data.getbest(preftype="mp4")  

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)

#it is 4 byte code which is use to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\YouTubeVdo.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Colorframe',frame)
        cv2.imshow("Gray Frame",gray)
        
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
