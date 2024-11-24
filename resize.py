import cv2 as cv

# Resize function_1 ->(Image,Video,Live videos)
def resize_image(frame, scale=0.75):
    width = int(frame.shape[1]*scale) # shape[1] represents width
    height = int(frame.shape[0]*scale) # shape[0] represents height

    dimentions = (width,height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_LINEAR)

# Inter_Area is useful to covert image from larger to smaller
# Inter_Linear || Inter_cubic is useful to covert imagefrom smaller to larger
# Cubic is slow method bt good method and clear method 

# Resize function_2 -> (Live videos)

# def resizeLive(width,height)
#     video.set(3,width) # width = 3
#     video.set(4,height) # Height = 4

#Resize photos

img = cv.imread('photos/cat.jpg')
cv.imshow('a',img)
resize = resize_image(img)
cv.imshow('Resize_a',resize)
cv.waitKey(0)

#Resize videos

# video = cv.VideoCapture('videos/cat.mp4')
# while True:
#     isTrue, frame = video.read()
#     frame_resized = resize_image(frame,scale=.25)

#     cv.imshow('Video',frame)
#     cv.imshow('Video_resize',frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('e'):
#         break

# video.release()
# cv.destroyAllWindows()