import cv2 as cv
import numpy as np

img = cv.imread('photos/paris2.jpg')
cv.imshow("Paris",img)

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('C_Blue',blue)
cv.imshow('C_Green',green)
cv.imshow('C_Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)