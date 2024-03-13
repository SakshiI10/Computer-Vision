import cv2
print("Package imported")

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Shapes.PNG")
img = cv2.resize(img, (400, 300))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(img, 100, 100)
imgBlank = np.zeros_like(img)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)

#1:21:21

cv2.waitKey(0)