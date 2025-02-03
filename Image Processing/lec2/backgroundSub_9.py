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

fgbg = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame. If frame is read correctly, ret = True.
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Orig',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #clean_gray = cv2.GaussianBlur(gray, (5, 5), 0)
    fgmask = fgbg.apply(gray)
    cv2.imshow('foreground',fgmask)
 
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

