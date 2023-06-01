# File: compare_edges.py

import cv2 as cv
import numpy as np

image = cv.imread('../images/usa.png', cv.IMREAD_GRAYSCALE)

# Laplacian
image_laplacian = cv.Laplacian(image, ddepth=-1, ksize=5)

# Laplacian-of-Gaussian
image_blur = cv.GaussianBlur(image, ksize=(3, 3), sigmaX=0)
image_log = cv.Laplacian(image_blur, ddepth=-1, ksize=5)

result = np.hstack((image_laplacian, image_log))
cv.imwrite('usa_compare.jpg', result)
