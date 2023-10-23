# File: homography_test2.py
# https://github.com/spmallick/learnopencv/blob/master/Homography/homography2.py

# Insert an image inside other image

import cv2 as cv
import numpy as np


def mouseHandler(event, x, y, flags, param):
    global im_temp, pts_dst

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(im_temp, center=(x, y), radius=3, color=(0, 255, 255), thickness=5, lineType=cv.LINE_AA)
        cv.imshow("Image", im_temp)
        if len(pts_dst) < 4:
            pts_dst = np.append(pts_dst, np.array([[x, y]]), axis=0)


# Read in the image.
im_src = cv.imread('../images/book1.jpg')
height, width = im_src.shape[:2]

# Create a list of points.
pts_src = np.empty((0, 2), dtype=np.int32)
pts_src = np.append(pts_src, np.array([[0, 0]]), axis=0)
pts_src = np.append(pts_src, np.array([[width - 1, 0]]), axis=0)
pts_src = np.append(pts_src, np.array([[width - 1, height - 1]]), axis=0)
pts_src = np.append(pts_src, np.array([[0, height - 1]]), axis=0)

# Destination image
im_dst = cv.imread('../images/book2.jpg')

# Create a window
cv.namedWindow("Image", 1)

im_temp = im_dst
pts_dst = np.empty((0, 2), dtype=np.int32)

cv.setMouseCallback("Image", mouseHandler)

cv.imshow("Image", im_temp)
cv.waitKey(0)

tform, status = cv.findHomography(pts_src, pts_dst)
im_temp = cv.warpPerspective(im_src, tform, dsize=(width, height))

cv.fillConvexPoly(im_dst, pts_dst, color=0, lineType=cv.LINE_AA)
im_dst = im_dst + im_temp

cv.imshow("Image", im_dst)
cv.waitKey(0)
