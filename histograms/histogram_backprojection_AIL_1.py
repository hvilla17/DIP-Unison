# File: histogram_backprojection_AIL_1.py
# https://theailearner.com/2019/04/18/histogram-backprojection/

import cv2 as cv
import matplotlib.pyplot as plot
import numpy as np

# roi is the object or region of object we need to find
roi = cv.imread('../images/messi_roi.png')
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# target is the image we search in
target = cv.imread('../images/messi_target.png')
hsv_target = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# Plot roi and target
plot.figure()
plot.title('ROI')
roi_rgb = cv.cvtColor(roi, cv.COLOR_BGR2RGB)
plot.imshow(roi_rgb, interpolation='nearest')

plot.figure()
plot.title('Target image')
target_rgb = cv.cvtColor(target, cv.COLOR_BGR2RGB)
plot.imshow(target_rgb, interpolation='nearest')

# Find the histograms
M = cv.calcHist([hsv_roi], channels=[0, 1], mask=None, histSize=[180, 256],
                ranges=[0, 180, 0, 256])
I = cv.calcHist([hsv_target], channels=[0, 1], mask=None, histSize=[180, 256],
                ranges=[0, 180, 0, 256])

# Plot the histograms
M_norm = cv.normalize(M, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
I_norm = cv.normalize(I, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

plot.figure()
plot.xlabel('Saturation', fontweight='bold')
plot.ylabel('Hue', fontweight='bold')
plot.title('ROI Hue vs Saturation')
plot.imshow(M_norm, cmap='gray', interpolation='nearest')

plot.figure()
plot.xlabel('Saturation', fontweight='bold')
plot.ylabel('Hue', fontweight='bold')
plot.title('Target Hue vs Saturation')
plot.imshow(I_norm, cmap='gray', interpolation='nearest')

R = M / I

# Plot R
plot.figure()
plot.xlabel('Saturation', fontweight='bold')
plot.ylabel('Hue', fontweight='bold')
plot.title('R = M / I')
plot.imshow(R, interpolation='nearest')

h, s, v = cv.split(hsv_target)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsv_target.shape[:2])

# Plot B
plot.figure()
plot.title('B')
plot.imshow(B, interpolation='nearest')

# Apply a convolution with a circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, ksize=(5, 5))
cv.filter2D(B, ddepth=-1, kernel=disc, dst=B)
B = np.uint8(B)
cv.normalize(B, dst=B, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

# Use thresholding to segment out the region
ret, thresh = cv.threshold(B, thresh=10, maxval=255, type=cv.THRESH_BINARY)

# Overlay images using bitwise_and
thresh = cv.merge((thresh, thresh, thresh))
result = cv.bitwise_and(target, thresh)

# Display the output
plot.figure()
plot.title('Result')
result_rgb = cv.cvtColor(result, cv.COLOR_BGR2RGB)
plot.imshow(result_rgb, interpolation='nearest')

plot.show()
