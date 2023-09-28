# File: histogram_backprojection_AIL_2.py
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

# Calculating object histogram
M = cv.calcHist(images=[hsv_roi], channels=[0, 1], mask=None, histSize=[180, 256],
                ranges=[0, 180, 0, 256])

# Normalize histogram and apply backprojection
cv.normalize(M, dst=M, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
B = cv.calcBackProject(images=[hsv_target], channels=[0, 1], hist=M,
                       ranges=[0, 180, 0, 256], scale=1)

# Apply a convolution with a circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, ksize=(5, 5))
cv.filter2D(B, ddepth=-1, kernel=disc, dst=B)
B = np.uint8(B)
cv.normalize(B, dst=B, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)

# Use thresholding to segment out the region
ret, thresh = cv.threshold(B, thresh=10, maxval=255, type=0)

# Overlay images using bitwise_and
thresh = cv.merge((thresh, thresh, thresh))
result = cv.bitwise_and(target, thresh)

# Display the output
plot.figure()
plot.title('ROI')
roi_rgb = cv.cvtColor(roi, cv.COLOR_BGR2RGB)
plot.imshow(roi_rgb, interpolation='nearest')

plot.figure()
plot.title('target')
target_rgb = cv.cvtColor(target, cv.COLOR_BGR2RGB)
plot.imshow(target_rgb, interpolation='nearest')

plot.figure()
plot.title('Result')
result_rgb = cv.cvtColor(result, cv.COLOR_BGR2RGB)
plot.imshow(result_rgb, interpolation='nearest')

plot.show()
