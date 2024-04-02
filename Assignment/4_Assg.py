import cv2
import numpy as np

# Load image
image = cv2.imread("D:\\My codes\\Computer Vision\\Assignment\\helmet2.jpeg")

# Convert image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for the yellow color (HSV range)
lower_yellow = np.array([20, 100, 100])  # Lower bound for hue, saturation, and value
upper_yellow = np.array([40, 255, 255])  # Upper bound for hue, saturation, and value

# Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw bounding boxes around detected helmets
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the result
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
