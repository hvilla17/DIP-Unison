# File: histogram.py
import cv2 as cv

image = cv.imread('../images/MyPic.png', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
hist = cv.calcHist([image], [0], None, [256], [0, 256])
# hist is a 256x1 array
