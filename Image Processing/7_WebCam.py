import cv2
print("Package imported")

cap = cv2.VideoCapture(0)
# Define width i.e. ID no. 3
cap.set(3, 640)
# Define height i.e. ID no. 4
cap.set(4, 480)
# Change brightness i.e. ID no. 10
cap.set(10, 100)
while True:
    success, vdo = cap.read()
    cv2.imshow("Video", vdo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 