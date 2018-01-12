import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret,new_img = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY) 
#adjust the value of last parameter to get better image quality 
new_img = cv2.adaptiveThreshold(img2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
cv2.imshow('image',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
