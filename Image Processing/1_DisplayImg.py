import cv2
print("Package imported")

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Nature.jpg")
imgResize = cv2.resize(img, (640, 480))
cv2.imshow("Output", imgResize)
cv2.waitKey(0)
