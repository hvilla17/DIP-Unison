# File: perspective_correction.py
# https://github.com/spmallick/learnopencv/blob/master/Homography/perspective-correction.py


import cv2 as cv
import numpy as np

from utils import get_four_points

# Read in the image.
im_src = cv.imread("../images/book1.jpg")

# Destination image
size = (300, 400, 3)

# im_dst = np.zeros(size, np.uint8)

pts_dst = np.array(
    [
        [0, 0],
        [size[0] - 1, 0],
        [size[0] - 1, size[1] - 1],
        [0, size[1] - 1]
    ], dtype=float
)

print('''
        Click on the four corners of the book -- top left first and
        bottom left last -- and then hit ENTER
        ''')

# Show image and wait for 4 clicks.
cv.imshow("Image", im_src)
pts_src = get_four_points(im_src)

# Calculate the homography
h, status = cv.findHomography(pts_src, pts_dst)

# Warp source image to destination
im_dst = cv.warpPerspective(im_src, h, size[0:2])

# Show output
cv.imshow("Image", im_dst)
cv.waitKey(0)
