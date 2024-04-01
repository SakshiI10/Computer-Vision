import cv2

cap = cv2.VideoCapture("D:/My codes/Computer Vision/Image Processing/Resources/NatureV.mp4")
print(cap)

while True:
    success, vdo = cap.read()
    vdo=cv2.resize(vdo,(500,500))
    cv2.imshow("Video", vdo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()  