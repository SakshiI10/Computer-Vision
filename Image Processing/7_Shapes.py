import cv2
import numpy as np

# To draw a shapped image
img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)
print(img)

# To color whole image
# img[:]=255,0,0
# To color a shape: [height, width]
# img[200:300, 100:300] = 255, 0, 0

# To create line: (image, starting point/width, ending point/height, color code, thickness)
cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),3)

# To create a rectangle: (image, starting point, ending or diagonal point, color code, thickness)
cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED)

# To create circles: (image, centre, radius, color code, thickness)
cv2.circle(img, (400,50), 30, (255, 255,0), cv2.FILLED)

cv2.imshow("Image", img)
cv2.waitKey(0)