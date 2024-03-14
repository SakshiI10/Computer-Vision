# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:27:08 2024

@author: SMI
"""

import cv2

vidcap = cv2.VideoCapture("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\NatureV.mp4")
#READ THE VIDEO
ret,image = vidcap.read()
count = 0

while True:
  if ret == True:
      # save frame as JPEG file
      cv2.imwrite("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\Frames\\imgN%d.jpg" % count, image)

      #used to hold speed of frane generation
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100)) 
      
      ret,image = vidcap.read()
      cv2.imshow("res",image)
      print ('Read a new frame:',count ,ret)
      count += 1
      
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break
          cv2.destroyAllWindows()


vidcap.release() 
cv2.destroyAllWindows()  