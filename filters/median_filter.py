# File: median_filter.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/salt_and_pepper.png', cv.IMREAD_COLOR)
image_blur = cv.medianBlur(image, ksize=7)
result = np.hstack((image, image_blur))
cv.imwrite('salt_and_pepper_median.png', result)
