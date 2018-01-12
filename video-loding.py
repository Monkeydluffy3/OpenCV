import cv2
import numpy as np

#to start the camera 
cap = cv2.VideoCapture(0)
#to record the video we initalize video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))
while True:
   
    ret,  frame = cap.read()  #to read frame from camera
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert the frame capture to gray frame
    cv2.imshow('video',frame)
    cv2.imshow('gray',gray)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
      break
      
cap.release()  #release the camera 
out.release()
cv2.destroyAllWindows()      
