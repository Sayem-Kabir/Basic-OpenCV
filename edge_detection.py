import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

##### Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

##### Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)

cv.imshow("Sobel_x",sobel_x)
cv.imshow("Sobel_y",sobel_y)
cv.imshow("Combined_sobel",combined_sobel)

##### Canny
canny = cv.Canny(gray,150,175)
cv.imshow("Canny",canny)

cv.waitKey(0)