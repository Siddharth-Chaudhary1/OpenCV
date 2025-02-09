import cv2 as cv
import numpy as np

def resizeImage(img, scale=0.1):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Cat', resizeImage(img))

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x ---> left
# -y ---> up
# +x ---> Right
# +y ---> Down

translated = translate(img, -100, 100)
# cv.imshow('Translated', resizeImage(translated))

# Rotation 
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # point about which image will rotate
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    # this return the rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 is scale
    dimensions = (width,height)

    # this multiplies the rotation matrix with the image
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
# cv.imshow('Rotated', resizeImage(rotated))

# flip the image -1 vertically
flip = cv.flip(img, 1)
cv.imshow('flip', resizeImage(flip))

cv.waitKey(0)