import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
#cv.imshow("Cat",img)

### From (img, grey, blur) to (edge_detection(canny)) to find contours
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("grey",grey)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
#cv.imshow("Blur",blur)

edge = cv.Canny(img, 125, 150)
#cv.imshow("Edge",edge)

edge_blur = cv.Canny(blur, 125, 150)
#cv.imshow("Edge_blur",edge_blur)

contours, hierarchies = cv.findContours(edge_blur,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours)} contour(s) found!')

## RETR_LIST --> find all the contours inside an img
## RETR_EXTERNAL --> returns all the external contours
## RETR_TREE --> return all the hierarchals contours

### From img to grey to threshold to find contours
### Threshold function to binarize the img
ret, thresh = cv.threshold(grey,125,255,cv.THRESH_BINARY)
#cv.imshow("Thresh", thresh)   #thresh need to have grey scale

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours)} contour(s) found!')



### After finding contours we can draw the contours in an image 
blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank',blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
#cv.imshow("Contours Draw",blank)


cv.waitKey(0)