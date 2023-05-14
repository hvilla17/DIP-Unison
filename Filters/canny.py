import cv2 as cv
import numpy as np

image = cv.imread('valve_original.png', cv.IMREAD_GRAYSCALE)
edges = cv.Canny(image, 50, 170)
result = np.hstack((image, edges))
cv.imwrite('valve_original_canny.png', result)
