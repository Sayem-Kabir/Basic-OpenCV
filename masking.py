import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('Dog',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
#cv.imshow('Blank',blank)

### we can create any shapes with bitwise fuction and mask it
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#cv.imshow('mask_blank',mask)

mask_img = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked_img",mask_img)

cv.waitKey(0)