# File: clahe.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/tsukuba_gray.png', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(image)
result = np.hstack((image, image_clahe))  # stacking images side-by-side
cv.imwrite('tsukuba_clahe.png', result)
