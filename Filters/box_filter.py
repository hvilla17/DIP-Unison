# File: box_filter.py
import cv2 as cv
import numpy as np

image = cv.imread('salt_and_pepper.png', cv.IMREAD_COLOR)
image_blur = cv.blur(image, ksize=(7, 7), borderType=cv.BORDER_CONSTANT)
result = np.hstack((image, image_blur))
cv.imwrite('salt_and_pepper_box.png', result)
