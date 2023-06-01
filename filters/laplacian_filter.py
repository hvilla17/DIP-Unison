# File: laplacian_filter.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/usa.png', cv.IMREAD_GRAYSCALE)
image_edges = cv.Laplacian(image, ddepth=-1, ksize=5)
result = np.hstack((image, image_edges))
cv.imwrite('usa_laplacian.png', result)
