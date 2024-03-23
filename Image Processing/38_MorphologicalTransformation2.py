import cv2
import numpy as np
from matplotlib import pyplot as plt

img_path = "D:\\My codes\\Computer Vision\\Image Processing\\Resources\\col_balls.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Check if the image has been successfully loaded
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

# Threshold the image
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# Define the kernel for morphological operations
kernel = np.ones((3, 3), np.uint8)

# Opening: Erosion followed by Dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Closing: Dilation followed by Erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Morphological operations to demonstrate different effects
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)   # Difference between mask and opening
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)  # Difference between dilation and erosion
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)  # Difference between closing and mask

# Show the images
titles = ["Original", "Mask", "Opening", "Closing", "Top Hat", "Gradient", "Black Hat"]
images = [img, mask, opening, closing, tophat, gradient, blackhat]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
