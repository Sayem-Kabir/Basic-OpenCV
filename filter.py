import cv2 as cv

img = cv.imread('photos/naruto.jpg')
cv.imshow('naruto',img)

### Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

### Convert to Blur
blur = cv.GaussianBlur(img,(11,11),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

### Creating Edge Cascade
edge = cv.Canny(img,125,175) 
cv.imshow("Edge Dectection",edge)

edge = cv.Canny(blur,125,175) # remove edge
cv.imshow("Edge Dectection",edge)

### Dilating the image -> work with edge
dilated = cv.dilate(edge,(5,5),iterations=3)
cv.imshow("Dilated",dilated)

### Eroded -> work with edge
eroded = cv.erode(blur,(3,3),iterations=1)
#cv.imshow("Eroded",eroded)

### Cropping
crop = img[50:200, 200:600]
cv.imshow("Crop",crop)

cv.waitKey(0)