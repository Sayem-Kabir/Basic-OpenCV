import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

### bitwise and --> intersecting
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise_and",bitwise_and)

### bitwise or --> both intersectring and non intersecting
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise_or",bitwise_or)

### bitwise xor --> non intersecting 
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise_xor",bitwise_xor)

### bitwise not --> invert
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise_rectangle_not",bitwise_not)

cv.waitKey(0)