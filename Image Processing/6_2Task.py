# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:17:24 2024

@author: SMI
"""
# Convert Video to Gray Colored
import cv2

cap = cv2.VideoCapture("D:/My codes/Computer Vision/Image Processing/Resources/NatureV.mp4")
print(cap)

while True:
    success, vdo = cap.read()
    vdo=cv2.resize(vdo,(500,500))
    gray=cv2.cvtColor(vdo,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Video", vdo)
    cv2.imshow("Gray Colored Video", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()