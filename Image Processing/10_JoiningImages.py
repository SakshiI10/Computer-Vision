import cv2
import numpy as np

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Gateway.jpg")
# img = cv2.resize(img, (300, 200))

''' #Join Images
imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))

cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)
cv2.waitKey(0) '''

''' 
Problems:
1) Can't Resize
2) Both the images need to have same channel(eg, RGB, Gray, etc)

View Solution on next page.
'''