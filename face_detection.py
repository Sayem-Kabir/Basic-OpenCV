import cv2 as cv

img = cv.imread('photos/group2.jpg')
cv.imshow('group2',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray_Baby",gray)

haar_cascade = cv.CascadeClassifier('hear_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print (f'Number of faces found = {len(faces_rect)}')

for(x,y,w,z) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+z),(0,255,0),thickness=2)

cv.imshow("Detect Faces",img)
cv.waitKey(0)