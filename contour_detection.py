import cv2 as cv
import numpy as np

def resizeImage(img, scale=0.09):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/cat1.jpg')
cv.imshow('Cat', resizeImage(img))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', resizeImage(gray))

canny = cv.Canny(img, 125, 125)
# cv.imshow('Canny', resizeImage(canny))

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

'''
Contours are simply boundaries of objects detected in the image.
cv.findContours() detects these boundaries.

Parameters

1) canny → Binary image (edges detected).
2) cv.RETR_LIST → Contour retrieval mode:
   cv.RETR_EXTERNAL: Retrieves only outermost contours.
   cv.RETR_TREE: Retrieves all contours and builds a hierarchy.
   cv.RETR_LIST: Retrieves all contours but does not store hierarchy.
3) cv.CHAIN_APPROX_NONE → Contour approximation method:
   cv.CHAIN_APPROX_NONE: Stores all contour points (detailed but slow).
   cv.CHAIN_APPROX_SIMPLE: Removes unnecessary points (saves memory).

Use cv.CHAIN_APPROX_SIMPLE unless you need every single point.
'''

# other ways to find contour using threshold
ret, thresh = cv.threshold(gray, 125, 125, cv.THRESH_BINARY)

'''
Parameters

1) gray → Grayscale input image.
2) 125 → Threshold value.
3) 125 → Maximum pixel value (ignored in some modes).
4) cv.THRESH_BINARY → Thresholding type:
   cv.THRESH_BINARY: Pixels > 125 → White (255), Pixels ≤ 125 → Black (0).
   cv.THRESH_BINARY_INV: Inverse of the above.
   cv.THRESH_TRUNC: Pixels > 125 are set to 125, rest remain unchanged.
   cv.THRESH_TOZERO: Pixels ≤ 125 become 0, rest unchanged.
'''

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')
# cv.imshow('contour', resizeImage(thresh))

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', resizeImage(blank))

# this draws contours over image -1 for all contours
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', resizeImage(blank))

cv.waitKey(0)