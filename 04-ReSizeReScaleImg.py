import cv2 as cv
import numpy as np


# we will create a FUNCTION (def) to rescale so that we can recal.. 
# this cv.resize() works for IMAGES - VIDEOS - LIVE VIDEO

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)      # .shape[1] => '1' means width of img!!
    height = int(frame.shape[0] * scale)     # .shape[0] => '0' means height of img!!

    # both height and width are integers, but get assigend as a float, thus we cahnge them to integers

    dimensions = (width,height)     # we created a tuple!

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# we will create a FUNCTION (def) to rescale 
# this cv.resize() works ONLY for LIVE VIDEO!!! it does not work with saved image or video. If you wan to change resolution 
# of a saved image or video - use -> cv.resize() cmd above!

def changeRes(width,height):
    capture.set(3,width)                    # 3 references width
    capture.set(4,height)                   # 4 references height // i.e. refrences brightness!


# resize image

img = cv.imread('/Users/mehmetugur/Documents/PythonOpenCV/Photos/Kenan.png')
cv.imshow('Original Iamge', img)
resized_image = rescaleFrame(img)
cv.imshow ('Resized Image', resized_image)

# reading video

capture = cv.VideoCapture('Videos/Tracker.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized1 = rescaleFrame(frame) # this uses paramterers as function abv 
    frame_resized2 = rescaleFrame(frame, scale=0.15) # this line gives scale specifc value under the function!

    cv.imshow('Video', frame)
    cv.imshow('Video Resized2', frame_resized1)
    cv.imshow('Video Resized3', frame_resized2)

    if cv.waitKey(20) & 0xFF==ord('d'):  #this 0xFF is keyboard entry
        break
capture.release()
cv.destroyAllWindows()



