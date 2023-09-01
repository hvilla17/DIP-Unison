# File: bilateral_salt_pepper.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/salt_and_pepper.png', cv.IMREAD_COLOR)
image_blur = cv.bilateralFilter(image, d=9, sigmaColor=500, sigmaSpace=5)
result = np.hstack((image, image_blur))
cv.imwrite('bilateral_salt_and_pepper.png', result)
