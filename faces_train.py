import os
import cv2 as cv
import numpy as np

people = ['Ed Sheeran','Jackie Chan','Lionel Messi','Robert Downey Jr','Taylor Swift']
DIR = r'D:\Self\opencv\Faces'

haar_cascade = cv.CascadeClassifier('hear_face.xml')


features = []
lebels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        lebel = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            #gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(img_array, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,z) in faces_rect:
                faces_roi = img_array[y:y+z,x:x+w]
                features.append(faces_roi)
                lebels.append(lebel)



create_train()

features = np.array(features,dtype='object')
lebels = np.array(lebels)

face_recognition = cv.face.LBPHFaceRecognizer_create()
face_recognition.train(features,lebels)
#face_recognition.save('face_trained.yml')
np.save('features.npy',features)
np.save('lebels.npy',lebels)

cv.waitKey(0)