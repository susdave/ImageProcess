import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

#We can't combine the 3 color detector in one frame so we decide to create 3 different python files
#The colors are red,blue,green
#Here is the color red
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_b = np.array([150,150,0])
    red_d = np.array([180,255,255])

    mask = cv2.inRange(hsv, red_b,red_d)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('red',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
