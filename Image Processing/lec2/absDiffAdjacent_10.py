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
	
ret, current_frame = cap.read()
previous_frame = current_frame

# Read until video is completed
while(cap.isOpened()):
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    previous_frame_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)    

    frame_diff = cv2.absdiff(current_frame_gray,previous_frame_gray)
    ret, thresh_frame_diff = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)

    previous_frame = current_frame.copy()
    ret, current_frame = cap.read()

 
    cv2.imshow("Previous frame", previous_frame)
    cv2.imshow("Current", current_frame)
    cv2.imshow("Adjacent difference", frame_diff)
    cv2.imshow("Thresholded adjacent difference", thresh_frame_diff)
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

