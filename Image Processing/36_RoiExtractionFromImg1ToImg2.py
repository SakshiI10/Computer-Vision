# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:02:43 2024

@author: SMI
"""
#Roi extraction from any shaped 
import cv2

# Load two images
img1 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\hero1.jpg")
img2 = cv2.imread("D:\\My codes\\Computer Vision\\Image Processing\\Resources\\hero2.jpg")
img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I want to fix img2 data into img1
r,c,ch = img2.shape

#1) Roi of an image (y,x)
roi = img1[:r,:c]

#2) Now creating mask for img1
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#3) create mask using threshold
_, mask = cv2.threshold(img_gry, 50, 255, cv2.THRESH_BINARY)

#4) remove bg
mask_inv= cv2.bitwise_not(mask)

#5) put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#6) Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

#7) Put logo in ROI and modify the main image
res = cv2.add(img1_bg,img2_fg)

final = img1
final[0:r,0:c]= res   #final output

cv2.imshow("Step -1 gry",img_gry)
cv2.imshow("Step -2 Mask",mask)
cv2.imshow("Step -3 Mask_inv",mask_inv)
cv2.imshow("Step -4 Mask_bg",img1_bg)
cv2.imshow("Step -5 Mask fg",img2_fg)
cv2.imshow("Step -6 Res",res)
cv2.imshow("Step -7 FInal",final)

cv2.waitKey(0)
cv2.destroyAllWindows()
