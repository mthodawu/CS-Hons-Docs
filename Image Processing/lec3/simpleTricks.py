import numpy as np #shortened (used often)
import cv2 # always need this
import sys
 
img1 = cv2.imread("images/road.jpg")
img2 = cv2.imread("images/car2.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#img2_gray = cv2.GaussianBlur(img2_gray, (3,3), 0)

img2_gray = cv2.fastNlMeansDenoising(img2_gray, None, 11, 7, 21)
img2_gray = cv2.bilateralFilter(img2_gray, 22, 45, 45)

#img2_gray = cv2.medianBlur(img2_gray, 21)

#ret,mask = cv2.threshold(img2_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
ret, mask = cv2.threshold(img2_gray, 242, 255, cv2.THRESH_BINARY)
#mask = cv2.adaptiveThreshold(img2_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)

mask_inv = cv2.bitwise_not(mask)
 
road = cv2.bitwise_and(img1, img1, mask=mask)
car = cv2.bitwise_and(img2, img2, mask=mask_inv)
addition = cv2.add(road, car)
weightedAddition = cv2.addWeighted(road,1.0,car,1.0,0)
hStack = np.hstack((img1,img2)) #stacking images side-by-side
hStack1 = np.hstack((mask,mask_inv)) #stacking images side-by-side
hStack2 = np.hstack((img1,img2,addition,weightedAddition)) #stacking images side-by-side


#fres = np.vstack((hStack1)) #stacking images side-by-side
#cv2.imshow('road, car',hStack)
cv2.imshow('carmask, not carmask',hStack1)
cv2.imshow('road, car, addition',hStack2)
cv2.waitKey(0)

cv2.destroyAllWindows()
