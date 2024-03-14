import cv2

faceCascadde = cv2.CascadeClassifier("D:/My codes/Computer Vision/Image Processing/Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Face.jpg")
img = cv2.resize(img, (400, 400))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascadde.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Output", img)
cv2.waitKey(0)
