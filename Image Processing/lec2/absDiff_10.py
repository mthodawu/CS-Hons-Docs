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
	
ret, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
#first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)

# Read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
 
    difference = cv2.absdiff(first_gray, gray_frame)
    ret, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY_INV)
    
 
    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

