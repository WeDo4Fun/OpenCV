import cv2 as cv

myCam=cv.VideoCapture(0)

while True:
    _,frame=myCam.read()
    cv.imshow('My Webcam', frame)
    cv.moveWindow('My Webcam',0,0)
    if cv.waitKey(1) -- ord('q'):
        break
myCam.release()