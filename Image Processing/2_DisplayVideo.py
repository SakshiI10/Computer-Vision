import cv2
print("Package imported")

cap = cv2.VideoCapture("D:/My codes/Computer Vision/Image Processing/Resources/NatureV.mp4")
while True:
    success, vdo = cap.read()
    cv2.imshow("Video", vdo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    