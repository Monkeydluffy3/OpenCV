import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("love.png",0)
#2nd parameter specify type of read
# 0 = cv2.IMREAD_GRAYSCALE
#-1 = cv2.IMREAD_UNCHANGED
# 1 = cv2.IMREAD_COLOR
# remain blank for default parameter
# we usually convert image into grayscale format so that it is easy to analysis the image because color image has too many data to anyalzie

#cv2.imshow('Luffy',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#to plot image using matplotlib
plt.imshow(img,cmap='gray',interpolation = 'bicubic')
plt.plot([20,25],[78,69],'c',linewidth=10) #to draw any line on a image 
plt.show()
