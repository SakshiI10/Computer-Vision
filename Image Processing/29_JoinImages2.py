import cv2
import numpy as np

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0][0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (width, height))

                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows

        for x in range(rows):
            for y in range(cols):
                hor[x] = np.hstack((hor[x], imgArray[x][y]))
            hor_con[x] = cv2.resize(hor[x], (0, 0), None, scale, scale)

        ver = np.vstack(hor_con)

    else:
        for x in range(rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (width, height))

            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)

        hor = np.hstack(imgArray)
        ver = cv2.resize(hor, (0, 0), None, scale, scale)

    return ver

img = cv2.imread("D:/My codes/Computer Vision/Image Processing/Resources/Gateway.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgStack=stackImages(0.5,([img,img,img],[img,img,img]))
cv2.imshow("Image Stack", imgStack)
cv2.waitKey(0)