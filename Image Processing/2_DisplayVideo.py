import cv2
print("Package imported")

video_path = "D:/My codes/Computer Vision/Image Processing/Resources/Nature2.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    success, vdo = cap.read()

    if not success:
        print("Error: Failed to read frame.")
        break

    cv2.imshow("Video", vdo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()