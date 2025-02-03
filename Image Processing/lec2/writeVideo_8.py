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
	
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outVid.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
#Create and move windows to set locations
cv2.namedWindow('Orig',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('Grey',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('HSV',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Orig", 0,0);
cv2.moveWindow("Grey", 1280,0);
cv2.moveWindow("HSV", 0,600);
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Orig',frame)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grey',grey)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV',hsv)
    
    out.write(hsv)
 
    # Press q on keyboard to  exit
    if cv2.waitKey(15) & 0xFF == ord('q'):
      break
 
  # Break the loop when video ends

  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()

