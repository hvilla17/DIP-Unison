# File: png-to-jpg.py

import cv2 as cv
import sys

image = cv.imread('MyPic.png')
if image is None:
    print('Failed to read image from file')
    sys.exit(1)
success = cv.imwrite('MyPic.jpg', image)
if not success:
    print('Failed to write image to file')
    sys.exit(1)
