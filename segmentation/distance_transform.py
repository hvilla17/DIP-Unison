# File: distance_transform.py
import cv2 as cv
import numpy as np

# Input image is already binary
image = np.zeros((1000, 1000), dtype=np.uint8)
image[200:800, 200:800] = 255
cv.imwrite('square_original.png', image)

# Create a binary image (not necessary for this image)
ret, thresh = cv.threshold(image, 127, 255, cv.THRESH_BINARY)

# Determine the distance transform
dist = cv.distanceTransform(thresh, cv.DIST_L2, 5)

# Normalize the image
norm = cv.normalize(dist, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
result = norm.astype(np.uint8)  # Not necessary for writing the image to a file

# Write the result
cv.imwrite('square_distance.png', result)
