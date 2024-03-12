import cv2
import numpy as np

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Nature.jpg")
kernel=np.ones((5, 5), np.uint8)

# To give Gray colour to the image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.resize(imgGray, (640, 480))

# To give blur effect to the image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# To add an edge detector: 2 thresholds: 100 and 100
imgCanny = cv2.Canny(img, 100, 100)
imgCanny = cv2.resize(imgCanny, (640, 480))

# Dilation
imgDilation = cv2.dilate(imgCanny, kernel, iterations=5)

# Erossion
imgErosion = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilation)
cv2.imshow("Eroded Image", imgErosion)
cv2.waitKey(0)