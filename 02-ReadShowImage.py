import cv2 as cv
import numpy as np

img = cv.imread ("/Users/mehmetugur/Documents/PythonOpenCV/Photos/Kenan.png")

cv.imshow("WindowName", img)
cv.waitKey(0)
cv.destroyAllWindows() 

