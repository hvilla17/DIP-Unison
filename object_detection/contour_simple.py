# File: contour_simple.py
import cv2 as cv
import numpy as np

image = np.zeros((700, 700), dtype=np.uint8)
image[150:550, 150:550] = 255
cv.imwrite('square.png', image)
ret, thresh = cv.threshold(image, thresh=127, maxval=255, type=0)
contours, hierarchy = cv.findContours(thresh, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
print(hierarchy)
print(contours)
color = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
output = cv.drawContours(color, contours, contourIdx=-1, color=(0, 255, 0), thickness=2)
cv.imwrite('square-contours.png', output)
