import cv2
import numpy as np

img = cv2.imread("D:\\My codes\\Computer Vision\\Assignment\\helmet2.jpeg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([40, 255, 255])
lower_blue = np.array([90, 100, 100])
upper_blue = np.array([130, 255, 255])

mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours_yellow:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    helmet_detected = True

for contour in contours_blue:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    helmet_detected = True                  
    
if helmet_detected:
    print("Person belongs to Group A")
else:
    print("Person does not belong to Group A")   
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()