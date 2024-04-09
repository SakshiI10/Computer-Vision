import cv2

# Load pre-trained models for helmet and jacket detection
helmet_cascade = cv2.CascadeClassifier(r"D:\\My codes\\Computer Vision\\Image Processing\\Cascade Files\\haarcascade_helmet.xml")
#jacket_cascade = cv2.CascadeClassifier('jacket_cascade.xml')

# Load image
image = cv2.imread("D:\\My codes\\Computer Vision\\Assignment\\helmet.jpeg")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect helmets
helmets = helmet_cascade.detectMultiScale(gray, 1.3, 4)

# Draw bounding boxes around detected helmets
for (x, y, w, h) in helmets:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Detect jackets
#jackets = jacket_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw bounding boxes around detected jackets
#for (x, y, w, h) in jackets:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
