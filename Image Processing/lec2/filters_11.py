#reads in a png image and filters it

import numpy as np #shortened (used often)
import cv2 # always need this
import sys

# image from command line arg
noisy = cv2.imread(sys.argv[1])
h, w = noisy.shape[:2]

#Create and move windows to set locations
cv2.namedWindow('Orig',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('gBlur',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('mBlur',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('bilateralFilter',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('fastNlMeansDenoising',cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Orig", 150,0)
cv2.moveWindow("gBlur", 0,350)
cv2.moveWindow("mBlur", 300,350)
cv2.moveWindow("bilateralFilter", 0,700 )
cv2.moveWindow("fastNlMeansDenoising", 300,700)

noisy = cv2.resize(noisy,(300,300))
cv2.imshow('Orig',noisy)


gBlur = cv2.GaussianBlur(noisy, (25, 25), 0)
mBlur = cv2.medianBlur(noisy, 15)
bil = cv2.bilateralFilter(noisy, 15, 150, 150)
nl = cv2.fastNlMeansDenoising(noisy, None, 22, 7, 21)


cv2.imshow('fastNlMeansDenoising',nl)
cv2.imshow('gBlur',gBlur)
cv2.imshow('mBlur',mBlur)
cv2.imshow('bilateralFilter',bil)
cv2.waitKey(0)
cv2.destroyAllWindows()
