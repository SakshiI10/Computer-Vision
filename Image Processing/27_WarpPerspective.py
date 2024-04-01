import cv2
import numpy as np

# Define the width and height for the output image
width, height = 150, 200

# Read the input image
img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Cards.jpeg")

# Define the source points (pts1) and destination points (pts2) for perspective transformation
pts1 = np.float32([[167, 35], [234, 44], [239, 109], [156, 100]])
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

# Calculate the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the perspective transformation to the original image
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

# Display the original and transformed images
cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

# Wait for a key press and close the windows
cv2.waitKey(0)
