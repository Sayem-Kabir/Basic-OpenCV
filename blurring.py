import cv2 as cv

img = cv.imread('photos/dog.jpg')
cv.imshow("dog",img)

##### Averaging Blur
average = cv. blur(img,(3,3))
cv.imshow("Average",average)

##### Gaussian blur
### Gaussian blur is less blur than average but it has more natural blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gauss",gauss)

##### Median Blur 
### this is more effective for clearing noise
### median blue is not meant for high cornal size like 7
median = cv.medianBlur(img,3)
cv.imshow("Median",median)

##### Bilateral Blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)