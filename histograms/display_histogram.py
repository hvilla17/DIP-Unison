# File: display_histogram.py
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/MyPic.png', cv.IMREAD_GRAYSCALE)

plt.hist(image.ravel(), 256, [0, 256])
plt.show()
