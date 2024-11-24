import cv2 as cv
import numpy as np

img = cv.imread("photos/cat.jpg")
cv.imshow("Cat",img)

### Translation -> shift an image
def translation(img,x,y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down    

translated = translation(img,100,100)
#cv.imshow("Transformation",translated)

### Rotation
def rotate(img, angle, rotation_point = None):
    (height, width) = img.shape[:2]

    if rotation_point is None:
            rotation_point = (width//2, height//2)
        
    rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotation_matrix, dimensions)

rotated = rotate(img,45)
#cv.imshow("Rotated",rotated)

rotation_again = rotate(rotated,45)
#cv.imshow("Rotatation again",rotation_again) ## creating extra black because roted already got black surface and rotated again assume those black spots as a part of the img

rotated = rotate(img,90) 
#cv.imshow("Rotated",rotated)

# + angle --> counter clockwise
# - angle --> clockwise

### Flip
flip = cv.flip(img,-1)
cv.imshow("flip",flip)

# 0 --> y axis 
# 1 --> x axis
# -1 --> both axis

cv.waitKey(0)