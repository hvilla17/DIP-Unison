# File: histogram_backprojection.py
import cv2 as cv
import numpy as np

debug = False

# Read image and select ROI
target = cv.imread('../images/messi5.jpg')
roi = target[270:330, 20:170]

if debug:
    cv.rectangle(target, pt1=(20, 270), pt2=(170, 330), color=(0, 255, 0), thickness=3)
    cv.imwrite('roi.jpg', target)
    cv.imwrite('roi-alone.jpg', roi)

# Convert to HSV
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
hsv_target = cv.cvtColor(target, cv.COLOR_BGR2HSV)

# Calculate ROI histogram
roi_hist = cv.calcHist(images=[hsv_roi], channels=[0, 1], mask=None, histSize=[180, 256],
                       ranges=[0, 180, 0, 256])

# Normalize histogram and apply backprojection
cv.normalize(src=roi_hist, dst=roi_hist, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
dst = cv.calcBackProject(images=[hsv_target], channels=[0, 1], hist=roi_hist,
                         ranges=[0, 180, 0, 256], scale=1)

# Convolute with circular disc
disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, ksize=(5, 5))
cv.filter2D(dst, ddepth=-1, kernel=disc, dst=dst)

# Threshold and binary AND
ret, thresh = cv.threshold(dst, thresh=50, maxval=255, type=cv.THRESH_BINARY)
thresh = cv.merge((thresh, thresh, thresh))
result = cv.bitwise_and(target, thresh)

result = np.vstack((target, thresh, result))
cv.imwrite('hist_backprojection.png', result)
