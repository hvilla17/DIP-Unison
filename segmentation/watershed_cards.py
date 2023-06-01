# File: watershed_cards.py
# https://docs.opencv.org/4.x/d2/dbd/tutorial_distance_transform.html
from __future__ import print_function
import cv2 as cv
import numpy as np
import random as rng

rng.seed(12345)

# [load_image]
# Load the image
src = cv.imread('../images/cards.png')
# [load_image]

# [black_bg]
# Change the background from white to black, since that will help later to extract
# better results during the use of Distance Transform
src[np.all(src == 255, axis=2)] = 0
cv.imwrite('01-black-background.png', src)
# [black_bg]

# [sharp]
# Create a kernel that we will use to sharpen our image
# an approximation of second derivative, a quite strong kernel
kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)

# do the laplacian filtering as it is
# well, we need to convert everything in something deeper than CV_8U
# because the kernel has some negative values,
# and we can expect in general to have a Laplacian image with negative values
# BUT a 8bits unsigned int (the one we are working with) can contain values from 0 to 255
# so the possible negative number will be truncated
imgLaplacian = cv.filter2D(src, ddepth=cv.CV_32F, kernel=kernel)
sharp = np.float32(src)
imgResult = sharp - imgLaplacian

# convert back to 8 bits gray scale
imgResult = np.clip(imgResult, 0, 255)
imgResult = imgResult.astype('uint8')
imgLaplacian = np.clip(imgLaplacian, 0, 255)
imgLaplacian = np.uint8(imgLaplacian)

cv.imwrite('02-Laplace.png', imgLaplacian)
cv.imwrite('03-sharpened.png', imgResult)
# [sharp]

# [bin]
# Create binary image from source image
bw = cv.cvtColor(imgResult, cv.COLOR_BGR2GRAY)
_, bw = cv.threshold(bw, thresh=40, maxval=255, type=cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imwrite('04-binary.png', bw)
# [bin]

# [dist]
# Perform the distance transform algorithm
dist = cv.distanceTransform(bw, distanceType=cv.DIST_L2, maskSize=3)
# Normalize the distance image for range = {0.0, 1.0}
# so we can visualize and threshold it
cv.normalize(dist, dst=dist, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
temp = cv.normalize(dist, dst=None, alpha=0, beta=255.0, norm_type=cv.NORM_MINMAX)
cv.imwrite('05-distances.png', temp)
# [dist]

# [peaks]
# Threshold to obtain the peaks
# This will be the markers for the foreground objects
_, dist = cv.threshold(dist, thresh=0.4, maxval=1.0, type=cv.THRESH_BINARY)

# Dilate a bit the dist image
kernel1 = np.ones((3, 3), dtype=np.uint8)
dist = cv.dilate(dist, kernel=kernel1)
temp = cv.normalize(dist, dst=None, alpha=0, beta=255.0, norm_type=cv.NORM_MINMAX)
cv.imwrite('06-peaks.png', temp)
# [peaks]

# [seeds]
# Create the CV_8U version of the distance image
# It is needed for findContours()
dist_8u = dist.astype('uint8')

# Find total markers
contours, _ = cv.findContours(dist_8u, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)

# Create the marker image for the watershed algorithm
markers = np.zeros(dist.shape, dtype=np.int32)

# Draw the foreground markers
for i in range(len(contours)):
    cv.drawContours(markers, contours=contours, contourIdx=i, color=(i + 1), thickness=-1)

# Draw the background marker
cv.circle(markers, center=(5, 5), radius=3, color=(255, 255, 255), thickness=-1)
markers_8u = (markers * 10).astype('uint8')
cv.imwrite('07-markers.png', markers_8u)
# [seeds]

# [watershed]
# Perform the watershed algorithm
cv.watershed(imgResult, markers=markers)

# mark = np.zeros(markers.shape, dtype=np.uint8)
mark = markers.astype('uint8')
mark = cv.bitwise_not(mark)
# uncomment this if you want to see how the mark
# image looks like at that point
cv.imwrite('07-markers_v2.png', mark)

# Generate random colors
colors = []
for contour in contours:
    colors.append((rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256)))

# Create the result image
dst = np.zeros((markers.shape[0], markers.shape[1], 3), dtype=np.uint8)

# Fill labeled objects with random colors
for i in range(markers.shape[0]):
    for j in range(markers.shape[1]):
        index = markers[i, j]
        if 0 < index <= len(contours):
            dst[i, j, :] = colors[index - 1]

# Write the final image
cv.imwrite('08-result.png', dst)
# [watershed]
