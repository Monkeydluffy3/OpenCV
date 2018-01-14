#Using GrabCut Algorithm 
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi.jpg')  #loading image from file

#cv2.rectangle(img,(350,40),(600,580),(255,255,0),5)  #finding the area of intrest(forground area) using hit and trail method 
rect = (350,40,600,580)

mask = np.zeros(img.shape[:2],np.uint8)
#what it does ? -> the img.shape[:3] return three parameter length,breath and degree of gamma factor(which is not of our use) so we use [:2] insted of [:3] . let say it reutrn (265,560) so the np.zeros initalize 2D array of integer type of given size 

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
#same as above explanation.these two must remain untuched for processing on same image.

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8') #if given mask is zero or 2 return 0 else 1
img = img*mask2[:,:,np.newaxis]

#grabcut function : what it really does is that it take input parameter as u can see in function where mask is our output(which we are concern about) and  rect area(area of intrest)  bgdModel,fgdModel used in intermediate purpose of image processing next parameter is no of iteration u want to perform on image(more time u perform more accurate result u get) 

#so as mask(2D array) is output (which represnt whether the pixel is forground or background) so at last we only need to print the forground image so we check whether the element of mask is 0 ot 2 then we make it as 1 otherwise 0

#then we multiply mask2 with image 
# as image is of three tuple so we need to add another tuple in the mask2 

cv2.imshow('messi',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
