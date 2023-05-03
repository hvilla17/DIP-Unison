# File: color-to-gray.png

import cv2 as cv
import sys

grayImage = cv.imread('MyPic.png', cv.IMREAD_GRAYSCALE)
if grayImage is None:
    print('Failed to read image from file')
    sys.exit(1)
success = cv.imwrite('MyPicGray.png', grayImage)
if not success:
    print('Failed to write image to file')
    sys.exit(1)
