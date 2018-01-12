import cv2
import numpy as np

#reading two image file from file
img1 = cv2.imread("graph1.png")
img2 = cv2.imread("graph2.png")


#add two image means superimposing two image
#add = img1 + img2
#add two image according to there weight 5th(last) parameter is degree of opecness(gamma factor) 
#add = cv2.addWeighted(img1,0.8,img2,0.2,10)

img3 = cv2.imread("logo.png")
row,col,channel =img3.shape #return shape and size of image
roi = img1[0:row , 0:col]

img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

#cv2.imshow("roi",img3)
#cv2.imshow("mask",mask)
img_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg = cv2.bitwise_and(img3,img3,mask=mask)

dst = cv2.add(img_bg,img_fg)

img1[0:row,0:col] = dst

cv2.imshow('result',img1)
cv2.imwrite('result.png',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
