# File: histogram_equalization_color.py

import cv2 as cv
import numpy as np

image = cv.imread('../images/9.bmp')

# equalize each channel
b, g, r = cv.split(image)
equ_b = cv.equalizeHist(b)
equ_g = cv.equalizeHist(g)
equ_r = cv.equalizeHist(r)
image_bgr = cv.merge((equ_b, equ_g, equ_r))

result = np.hstack((image, image_bgr))

cv.imwrite('9-equalized-bgr.bmp', result)

# convert the BGR image to YUV format
image_yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
image_yuv[:, :, 0] = cv.equalizeHist(image_yuv[:, :, 0])

# convert the YUV image back to BGR format
output = cv.cvtColor(image_yuv, cv.COLOR_YUV2BGR)

result = np.hstack((image, output))

cv.imwrite('9-equalized-yuv.bmp', result)
