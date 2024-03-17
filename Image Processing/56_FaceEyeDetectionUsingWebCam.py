# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:01:44 2024

@author: SMI
"""
import cv2

face=cv2.CascadeClassifier("D:\\My codes\\Computer Vision\\Image Processing\\Cascades\\haarcascade_frontalface_default.xml") #for detecting face
eye = cv2.CascadeClassifier("D:\\My codes\\Computer Vision\\Image Processing\\Cascades\\haarcascade_eye.xml") #for detecting eyes

def dector(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,125),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye.detectMultiScale(roi_gray,1.3,3)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.circle(roi_color,(ex+27,ey+27),20,(255,255,0),2)
    return img

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame =cap.read()
    frame = cv2.flip(frame,2)
    cv2.imshow("face dect",dector(frame))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()  