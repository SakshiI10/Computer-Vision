import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# To add a text: (Image, Text, Origin, Font, Font Size(Scale), Color, Thickness)
cv2.putText(img, "OPENCV", (200,200), cv2.FONT_HERSHEY_COMPLEX, 2, (0,150,0),2)

cv2.imshow("Image", img)
cv2.waitKey(0)