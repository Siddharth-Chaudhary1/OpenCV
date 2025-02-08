import cv2 as cv
import numpy as np

# creating blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# Point the image a certain colour
blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Blank', blank)

# draw rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness=2)
# cv.imshow('Rectangle', blank)

# draw circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2), 40, (0, 0, 255), thickness=-1)
# cv.imshow('Circel', blank)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[1]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# write text on img
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)