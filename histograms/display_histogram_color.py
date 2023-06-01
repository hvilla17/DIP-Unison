# File: display_histogram_color.py
import cv2 as cv
from matplotlib import pyplot as plot

image = cv.imread('../images/MyPic.png')
assert image is not None, "file could not be read, check with os.path.exists()"

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([image], [i], None, [256], [0, 256])
    plot.plot(histr, color=col)
    plot.xlim([0, 256])
plot.show()
