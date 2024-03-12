import cv2
import numpy as np

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Gateway.jpg")

print(img.shape)
# (3174, 3000, 3): 3174: height, 3000: width, 3: BGR(No of channels)
# To resize the image pixels (width, height)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)