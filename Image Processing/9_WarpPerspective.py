import cv2
import numpy as np

width,height = 250,350
img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Cards.jpeg")
pts1=np.float32([[167,35],[234,44],[239,109],[156,100]])
pts2=np.float32([[0,height],[width,height],[width,0],[0,0]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)
cv2.waitKey(0)