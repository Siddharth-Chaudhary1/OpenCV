import cv2 as cv

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dim = (width, height)

    return cv.resize(img, dim, interpolation = cv.INTER_AREA)

img = cv.imread('Photos/cat3.jpg')
cv.imshow('Cat', resizeImage(img))

# The kernel needs to have a center pixel
# to apply the convolution
# the kernel size must be odd numbers 

# Averaging: center value is the average 
#            of all the surrounding pixels
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', resizeImage(average))

# Gaussian Blur: center value is the weighted average
#                of all the surrounding pixels
gaussian = cv.GaussianBlur(img, (13, 13), 0)
cv.imshow('Gaussian Blur', resizeImage(gaussian))

# Median Blur: center value is the median
#              of all the surrounding pixels

# This is useful for removing salt and pepper noise
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', resizeImage(median))

# Bilateral: center value is the weighted average
#            of all the surrounding pixels
#            but the weights are calculated using
#            the intensity difference between the
#            center pixel and the surrounding pixels
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', resizeImage(bilateral))

cv.waitKey(0)