import numpy as np
import cv2
import sys

def drawMinEnclose(resized,circles):
    (x,y),radius = cv2.minEnclosingCircle(circles)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(resized,center,radius-1,(0,255,0),2)

# image from command line arg
imgFile = cv2.imread("lec3/images/realTarget.jpg",1)
cv2.imshow('Original', imgFile)
cv2.waitKey(0)

resized = cv2.resize(imgFile,(500,500))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

gray_blur = cv2.GaussianBlur(gray, (9, 9), 0)
ret,thresh = cv2.threshold(gray_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("OTSU Thresholding", thresh)
cv2.waitKey(0)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
# closing = cv2.dilate(thresh, kernel, iterations=2)
cv2.imshow("Morphological Closing", closing)
cv2.waitKey(0)

cont_img = closing.copy()
contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create a blank image for the bytemask... WHY named BYTE mask?
black = np.zeros(gray.shape)

for circles in contours:
	area = cv2.contourArea(circles)
	if area < 80 or area > 350:
			continue

	if len(circles) < 5:
			continue

	ellipse = cv2.fitEllipse(circles)
	drawMinEnclose(resized,circles)
	cv2.ellipse(black, ellipse, (255,255,255), -1, 2)
cv2.imshow('Contours', resized)
cv2.waitKey(0)

byteMask = np.asarray(black, dtype=np.uint8)
cv2.imshow('byteMask',byteMask)
cv2.waitKey(0)

holes = cv2.bitwise_and(gray, byteMask)
cv2.imshow('holes',holes)
cv2.waitKey(0)

cv2.destroyAllWindows()
