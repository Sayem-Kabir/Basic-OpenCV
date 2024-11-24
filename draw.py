import cv2 as cv
import numpy as np

# Creating a blank image
blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

# 1. Paint the whole image a certain colour
blank[:] = 0,0,0
#cv.imshow("Blue",blank)

# specific portion colour
blank[200:300, 300:400] = 0,0,255
#cv.imshow("Red",blank)

# 2. Rectangle border
cv.rectangle(blank,(100,100),(250,250),(255,255,255),thickness=2)
#cv.imshow("Rectangle",blank)

# Rectangle full
cv.rectangle(blank,(100,100),(250,250),(255,255,255),thickness=-1)
#cv.imshow("Rectangle",blank)

# half rectangle 
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=-1)
#cv.imshow("Half Rectangle",blank)

# 3. Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,255,200),thickness=-1)
#cv.imshow("Circle",blank)

# 4. Line
cv.line(blank,(250,250),(blank.shape[1],blank.shape[0]),(255,255,255),thickness=2)
#cv.imshow("Line",blank)

# 5. Text
cv.putText(blank,"HI! I am sayem",(0,225),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,2.0,(0,255,0),thickness=2)
#cv.imshow("Text",blank)

cv.waitKey(0)