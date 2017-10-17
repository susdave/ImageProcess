import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

#We can't combine the 3 color detector in one frame so we decide to create 3 different python files
#The colors are red,blue,green
#Here is the color blue
    
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue_b = np.array([97,100,117])
    blue_d = np.array([117,255,255])

    mask = cv2.inRange(hsv, blue_b, blue_d)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('blue',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
