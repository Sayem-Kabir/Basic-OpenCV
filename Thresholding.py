import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('Dog',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

##### Simple Thresholding
threshold, thresh = cv. threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple_threshold",thresh)

##### Inverse Simple Thresholding
threshold, thresh_inverse = cv. threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple_threshold_inverse",thresh_inverse)

##### Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 1)
cv.imshow("Adaptive Thresholding",adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 1)
cv.imshow("Adaptive Thresholding",adaptive_thresh)

cv.waitKey(0)