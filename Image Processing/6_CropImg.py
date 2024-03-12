import cv2
import numpy as np

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Gateway.jpg")

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)