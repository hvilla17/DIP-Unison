# File: display-histogram.py
import cv2 as cv
from matplotlib import pyplot as plot

image = cv.imread('MyPic.png', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
plot.hist(image.ravel(), 256, [0, 256])
plot.show()
