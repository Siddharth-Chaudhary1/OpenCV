'''
python -m venv opencv_env
opencv_env\Scripts\activate  # On Windows
pip install numpy opencv-python
python -c "import cv2; print(cv2.__version__)"
''' 

import cv2 as cv

# Read an image
img = cv.imread('Photos/cat2.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

