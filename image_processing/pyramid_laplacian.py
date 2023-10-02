# File: pyramid_laplacian.py
# https://theailearner.com/2019/08/19/image-pyramids/

import cv2 as cv

# Load the image
image = cv.imread('../images/lena-std.png')
lower = image.copy()

# Create a Gaussian Pyramid
gaussian_pyr = [lower]
for i in range(3):
    lower = cv.pyrDown(lower)
    gaussian_pyr.append(lower)

# Last level of Gaussian remains same in Laplacian
laplacian_top = gaussian_pyr[-1]

# Create a Laplacian Pyramid
laplacian_pyr = [laplacian_top]
for i in range(3, 0, -1):
    size = (gaussian_pyr[i - 1].shape[1], gaussian_pyr[i - 1].shape[0])
    gaussian_expanded = cv.pyrUp(gaussian_pyr[i], dstsize=size)
    laplacian = cv.subtract(gaussian_pyr[i - 1], gaussian_expanded)
    laplacian_pyr.append(laplacian)
    cv.imwrite('lap-{}.png'.format(i - 1), laplacian)
    cv.imshow('lap-{}'.format(i - 1), laplacian)
    cv.waitKey(0)
