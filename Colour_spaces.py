import cv2 as cv
##### Opencv reads color as BGR format

img = cv.imread('photos/cat.jpg')
cv.imshow("cat",img)


#### Conversion

### BGR to Grey
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

### BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

### BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB",lab)

### BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)


#### Reverse conversion

### HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv->bgr",hsv_bgr)

### LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab->bgr",lab_bgr)

##### There are only these methods for reverse conversion
##### so if we want to convert gray to lab then we need gray to bgr to lab



cv.waitKey(0)