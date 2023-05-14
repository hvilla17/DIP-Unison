# File: gaussian_filter.py
import cv2 as cv
import numpy as np

image = cv.imread('salt_and_pepper.png', cv.IMREAD_COLOR)
image_blur = cv.GaussianBlur(image, ksize=(7, 7), sigmaX=0, borderType=cv.BORDER_CONSTANT)
result = np.hstack((image, image_blur))
cv.imwrite('salt_and_pepper_gauss.png', result)
