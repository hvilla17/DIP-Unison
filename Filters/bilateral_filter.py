# File: bilateral_filter.py
import cv2 as cv
import numpy as np

image = cv.imread('salt_and_pepper.png', cv.IMREAD_COLOR)
image_blur = cv.bilateralFilter(image, d=9, sigmaColor=500, sigmaSpace=500)
result = np.hstack((image, image_blur))
cv.imwrite('salt_and_pepper_bilateral.png', result)
