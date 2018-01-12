import cv2
import numpy as np

cap = cv2.VideoCapture(0)    #capture the frame using main camera (camera number )

while True:
        
        _,frame = cap.read()   #read image from the camear 
        laplacian = cv2.Laplacian(frame,cv2.CV_64F) #this funcion take frame and data type as input and convert given frame into gradiant form because it is easy to detect edge from graident frame
        
       # conv = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #can try with gray scale format
        
        
        sobelx = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize = 3)   #adjust x,y(orientation of gradient) or size of gradiaent (3,4,5 resp.) paremeter 
        sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize = 3)
        
        edges = cv2.Canny(frame,80,150)
        
        cv2.imshow("orignal",frame)
        cv2.imshow("laplacian",laplacian)
        #cv2.imshow("sobelx",sobelx)
        #cv2.imshow("sobely",sobely)
        cv2.imshow('edges',edges)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
         break;
        
cap.release()
cv2.destroyAllWindows()        
        
