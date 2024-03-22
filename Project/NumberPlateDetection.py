# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:49:39 2024

@author: SMI
"""
import cv2

frameWidth = 500
frameHeight = 500
nPlateCascade = cv2.CascadeClassifier("D:\\My codes\\Computer Vision\\Image Processing\\Cascade Files\\haarcascade_russian_plate_number.xml")
minArea = 200
color = (255,0,255)

# Load image
img = cv2.imread("D:\\My codes\\Computer Vision\\Project\\Resources\\p3.jpg")
img = cv2.resize(img, (frameWidth, frameHeight))  # Resize image to specified frame dimensions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = 0

# Detect number plates
numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)

# Draw rectangles around detected number plates
for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
        imgRoi = img[y:y+h, x:x+w]
        cv2.imshow("ROI", imgRoi)

# Display the result
cv2.imshow("Result", img)

if cv2.waitKey(0) & 0xFF != ord('q'):
    cv2.imwrite("D:\\My codes\\Computer Vision\\Project\\Scanned Plates\\NoPlate_"+str(count)+".jpg",imgRoi)
    cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
    cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
    cv2.imshow("Result",img)
    cv2.waitKey(500)

cv2.destroyAllWindows()