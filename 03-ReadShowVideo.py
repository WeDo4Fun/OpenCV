import cv2 as cv
import numpy as np

capture = cv.VideoCapture('/Users/mehmetugur/Documents/PythonOpenCV/Videos/Tracker.mp4')

#  as reading video - with frames, has to run continously, we use "while True"!!

while True:
    isTrue, frame = capture.read() # this is a bolean, reads video frame by frame and is TRUE when can read a frame
    cv.imshow('Video Window', frame)

    if cv.waitKey (20) & 0xFF==ord('d'):    #wait for 20 milsec and cehck if 'd' is pressed (0xFF) -> break
        break

capture.release()
cv.destroyAllWindows()

# if we do not stop video by using 'd' and video runs out of frames - we have -215:assertion failed ERROR..  