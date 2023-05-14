# File: high_boost.py
import cv2 as cv
import numpy as np

image = cv.imread('soc-card.jpg')
mask = np.array([
    [0, -1, 0],
    [-1, 5.8, -1],
    [0, -1, 0]
])
smooth = cv.bilateralFilter(image, d=9, sigmaColor=9, sigmaSpace=7)
cv.imwrite('soc-card-smooth.jpg', smooth)
boost = cv.filter2D(smooth, ddepth=-1, kernel=mask)
result = np.hstack((image, boost))
cv.imwrite('soc-card-boost.jpg', result)
