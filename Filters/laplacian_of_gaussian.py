# File: laplacian_of_gaussian.py
import cv2 as cv
import numpy as np

image = cv.imread('usa.png', cv.IMREAD_GRAYSCALE)
image_blur = cv.GaussianBlur(image, ksize=(3, 3), sigmaX=0)
image_log = cv.Laplacian(image_blur, ddepth=-1, ksize=5)
result = np.hstack((image, image_log))
cv.imwrite('usa_log.jpg', result)
