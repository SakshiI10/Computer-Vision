# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:18:02 2024

@author: SMI
"""

import pyautogui as p
import cv2
import numpy as np

#Create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and Path: ")

output = cv2.VideoWriter(fn,*"XVID",60,rs)

#create recording module
cv2.namedWindow("Live_Recording",cv2.WINDOW_NORMAL)

#Resize the window
cv2.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot() #image
    f = np.array(img) #convert image into array
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    cv2.imshow("Live_Recording", f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

output.release() 
cv2.destroyAllWindows() 