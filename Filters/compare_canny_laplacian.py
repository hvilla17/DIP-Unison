import cv2 as cv
import numpy as np

image = cv.imread('valve_original.png', cv.IMREAD_GRAYSCALE)

# Laplacian-of-Gaussian
image_blur = cv.GaussianBlur(image, ksize=(3, 3), sigmaX=0)
image_log = cv.Laplacian(image_blur, ddepth=-1, ksize=5)

# Canny
edges = cv.Canny(image, 50, 170)

# Result
result = np.hstack((image_log, edges))
cv.imwrite('valve_original_compare.png', result)
