# File: watershed_no_overlap.py
import numpy as np
import cv2 as cv

image = cv.imread('../images/5_of_diamonds.png')

# Binarize the image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, thresh=0, maxval=255, type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imwrite('01_thresh.png', thresh)

# Remove noise
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(thresh, op=cv.MORPH_OPEN, kernel=kernel, iterations=2)
cv.imwrite('02_opening.png', opening)

# Find the sure background region
sure_bg = cv.dilate(opening, kernel=kernel, iterations=3)
cv.imwrite('03_sure_bg.png', sure_bg)

# Find the sure foreground region
dist = cv.distanceTransform(opening, distanceType=cv.DIST_L2, maskSize=5)
norm = cv.normalize(dist, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
cv.imwrite('04_distances.png', norm)
_, sure_fg = cv.threshold(dist, thresh=0.7 * dist.max(), maxval=255, type=0)
sure_fg = sure_fg.astype(np.uint8)
cv.imwrite('05_sure_fg.png', sure_fg)

# Find the unknown region
unknown = cv.subtract(sure_bg, sure_fg)
cv.imwrite('06_unknown.png', unknown)

# Label the foreground objects
_, markers = cv.connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers += 1

# Label the unknown region as 0
markers[unknown == 255] = 0

markers = cv.watershed(image, markers=markers)
image[markers == -1] = [255, 0, 0]

cv.imwrite('07_result_watershed.png', image)
