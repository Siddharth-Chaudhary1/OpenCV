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

# Read a video
capture = cv.VideoCapture('Videos/dog.mp4')

# run's the frame untill d is presseds
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()