# File: homography_book.py
# https://github.com/spmallick/learnopencv/blob/master/Homography/homography_book.py

# Align 2 books

import cv2 as cv
import numpy as np

# Read source image.
im_src = cv.imread('../images/book2.jpg')
# Four corners of the book in source image
pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], dtype=float)

# Read destination image.
im_dst = cv.imread('../images/book1.jpg')
# Four corners of the book in destination image.
pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]], dtype=float)

# Calculate Homography
h, status = cv.findHomography(pts_src, pts_dst)

# Warp source image to destination based on homography
im_out = cv.warpPerspective(im_src, h, dsize=(im_dst.shape[1], im_dst.shape[0]))

# Display images
cv.imshow("Source Image", im_src)
cv.imshow("Destination Image", im_dst)
cv.imshow("Warped Source Image", im_out)

cv.waitKey(0)
