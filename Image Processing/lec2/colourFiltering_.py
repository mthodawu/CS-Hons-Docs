#reads in a video from the first camera

import cv2
import numpy as np
import sys

# Create a VideoCapture object for video or file depending on command line arg
a = sys.argv[1]
if a == "0":
	cap = cv2.VideoCapture(0)
# Check if camera opened successfully
else:
	cap = cv2.VideoCapture(a)

while(cap.isOpened()):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([10,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()