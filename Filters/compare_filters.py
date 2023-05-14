# File: compare_filters.py
import cv2 as cv
import numpy as np

image = cv.imread('salt_and_pepper.png', cv.IMREAD_COLOR)
image_box = cv.blur(image, ksize=(7, 7), borderType=cv.BORDER_CONSTANT)
image_gauss = cv.GaussianBlur(image, ksize=(7, 7), sigmaX=0, borderType=cv.BORDER_CONSTANT)
image_median = cv.medianBlur(image, ksize=7)
image_bilateral = cv.bilateralFilter(image, d=9, sigmaColor=500, sigmaSpace=500)
t1 = np.hstack((image_box, image_gauss))
t2 = np.hstack((image_median, image_bilateral))
result = np.vstack((t1, t2))
cv.imwrite('salt_and_pepper_compare.png', result)
