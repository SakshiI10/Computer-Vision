import cv2
import numpy as np

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objectCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            
            if objectCorner == 3: 
                objectType = "Tri"
            elif objectCorner == 4: 
                aspectRatio = w / float(h)
                if 0.95 < aspectRatio < 1.05: 
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objectCorner>4: objectType="Circle"
            else: 
                objectType = "None"
            
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x + (x // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Shapes.PNG")
img = cv2.resize(img, (400, 300))
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 100, 100)
getContours(imgCanny, imgContour)
imgBlank = np.zeros_like(img)

cv2.imshow("Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Contour Image", imgContour)
cv2.waitKey(0)
