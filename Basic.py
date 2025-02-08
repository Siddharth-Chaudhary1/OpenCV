import cv2 as cv

def rescaleImage(img, scale=0.1):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Photos/cat1.jpg')
# cv.imshow('Cat', rescaleImage(img))

# converting to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', rescaleImage(grey))

# blur the image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', rescaleImage(blur))

# Edge Cascade: to find edge of image
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', rescaleImage(canny))

# dilate the image usign the canny img
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilate', rescaleImage(dilated))

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', rescaleImage(eroded))

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)