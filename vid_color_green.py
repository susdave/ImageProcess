import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

#We can't combine the 3 color detector in one frame so we decide to create 3 different python files
#The colors are red,blue,green
#Here is the color green
    
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    green_b = np.array([66,122,129])
    green_d = np.array([86,255,255])

    mask = cv2.inRange(hsv, green_b, green_d)
    res = cv2.bitwise_and(frame, frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('green',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
