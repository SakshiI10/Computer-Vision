# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:01:02 2024

@author: SMI
"""
# Show Height, Width, Date and Time on Video
import cv2
import datetime

cap = cv2.VideoCapture("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\NatureV.mp4")  
print("for width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("for height==",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 600)  #here 3 for width
cap.set(4, 800)  #here 4 for height 
print("Width====",cap.get(3))
print("Height===",cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       text = ' Height: ' + str(cap.get(4))+' Width: '+ str(cap.get(3))
       
       date_data = "Date: "+str(datetime.datetime.now())
       
       frame = cv2.putText(frame, text, (10, 20), font, 1, (0, 155, 255), 1, cv2.LINE_AA)
       frame = cv2.putText(frame, date_data, (20, 50), font, 1, (100, 255, 255), 1, cv2.LINE_AA)
       
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()