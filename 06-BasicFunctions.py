from csv import Dialect
import cv2 as cv

# i have used rescale as the origanl "Isabel" iamge was too big anf guassian blur was not effective! 

def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1] * scale)      # .shape[1] => '1' means width of img!!
    height = int(frame.shape[0] * scale)     # .shape[0] => '0' means height of img!!

    # both height and width are integers, but get assigend as a float, thus we cahnge them to integers

    dimensions = (width,height)     # we created a tuple!

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

imgOrig = cv.imread('/Users/mehmetugur/Documents/PythonOpenCV/Photos/Isabel.jpg')

img = rescaleFrame(imgOrig)

# 1. Convertign to GreyScale
# There are few ways, we will use cv.cvtColor(src/img, code, dst=None, dstCn=None, /)
# Orignal image .jpg is BRG Colors.. under CODE, we will use cv.COLOR_BGR2GRAY *** hv a lot of options here ***

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# 2. Blur - there are a lot of bluring METHODS. We will use 
# cv.GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None, /)
# KErnel size has to be an ODD number i.e. 1 3 5... etc 

blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# 3. Edge Cascade - we will use cv.Canny(img, treshold1, treshold2[, edges[, apertureSize[, L2gradient]]])

canny1 = cv.Canny(img, 125, 175)
canny2 = cv.Canny(img, 100, 5)
canny3 = cv.Canny(blur, 125, 175)

cv.imshow('Canny Original', canny1)
# cv.imshow('Canny Diff Param', canny2)
# cv.imshow('Canny Blurred', canny3) # blurred image gives less edges!! 

# 4. Dilating the image using cv.dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, boderValue=None)

dilated = cv.dilate(canny1, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding back fm dialtion using cv.Erode (src, kernel, dst=None,...)
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Erdoded', eroded)

# 6. Resize image usign cv.resize(src, dsize...) dsize = destiantion size!
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

# this 'resized' image will be out oaf aspect ratio! 
# also it works well when down sizing. in commande (at tback ground) it uses actaully 
# an 'interpolation=1' BUT if we want to upscale the image! we will need to use an alternative 
# interpolation => we can use" 
# - interpolation = cv.INTER_AREA // if we are shrinkign to smaller image 
# - interpolation = cv.INTER_LINEAR // or
# - interpolation = cv.INTER_CUBIC // takes longest to calc but gives best quality! 

# 7. Cropping: iamges are arrays and we can use array slicing to crop:
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

# Youtube at 44:09 

cv.waitKey(0)