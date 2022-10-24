import cv2 as cv
import numpy as np

# We can draw in images in 2 ways: 
# 1. We draw dirctly on image (like on Kenan.png), or
# 2. We create a blank (empty) dummy image 

# we are creating an empty image. in numpy datatype uint8 referst to image

blank = np.zeros((500,500,3), dtype='uint8')  #500,500,3: matrix works to width/deptb/color!

cv.imshow('Blank', blank)

# 1.1 Paint full image one color:

blank[:] = 0,255,0
cv.imshow('Green', blank)

# 1.2 Paisnt part of image in one color:

blank[:]=0,0,0   # we are reseting img to be black/blank
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red Box', blank)

# 2.1 Draw Rectangle usign cv.rectangel(img, pt1, pt2, color, thickness=None, lineType=None, shift=Non, /) METHOD

blank[:]=0,0,0   # we are reseting img to be black/blank
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle1', blank)

# 2.2 Draw a rectangle FILLED

blank[:]=0,0,0    # we are reseting img to be black/blank
cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness=cv.FILLED) # instead of cv.FILLED we can aso use '-1' below example
cv.imshow('Rectangle Filled',blank)

# 2.3 instead fo fixed coordinates like (0,0) or (250,500) above, we can also use iamge related parameters)

blank[:]=0,0,0
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
cv.imshow('Relative Parameters', blank)

# 3. Draw a cirlce using cv.circle(img, center, radius, color, thickness=None, linetype=None, shift=None, /)

blank[:]=0,0,0    # we are reseting img to be black/blank
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a line using cv.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None, /)

blank[:]=0,0,0
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=1)
cv.line(blank, (0,500), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=1)
cv.imshow('Line', blank)

# 5. Write Text - cv.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None, /)

blank[:]=0,0,0
cv.putText(blank, 'Hello World', (10,30), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,50), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,80), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,110), cv.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,140), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,170), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (0,255,0), 1)
cv.putText(blank, 'Hello World', (10,200), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 2)
cv.putText(blank, 'Hello World', (10,230), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 1)

cv.imshow('Text', blank)

cv.waitKey(0)