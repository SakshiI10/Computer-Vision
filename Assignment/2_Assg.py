import cv2
import numpy as np

def draw(event, x, y, flag, param):
    #print("x: ",x)
    #print("y: ",y)
    
    if event == cv2.EVENT_LBUTTONDOWN:
        #cordinates = ". "+ str(x) + ', '+ str(y)
        #cv2.putText(img, cord, (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (155,125 ,100), 2)
        cv2.rectangle(img,(x,y),(512, 512),(0,0,255),1)
        cv2.rectangle(img,(0,0),(x,y),(0,0,255),1)
        
        w = 512 - x
        h = 512 - y
        area1 = 2 * (x+y)
        area2 = 2 * (w + h)
        #print("Area:", area1)
        #print("Area:", area2)
        MaxArea=max(area1, area2)
        print("MaxArea: ", MaxArea)

cv2.namedWindow(winname = "Result")
img = np.zeros((512,512,3), np.uint8)
cv2.setMouseCallback("Result", draw)

while True:
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows() 
