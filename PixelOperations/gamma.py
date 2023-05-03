# File: gamma.py

import cv2 as cv
import numpy as np


def gamma_func(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    table = np.array([((i / 255.0) ** gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv.LUT(image, table)


image = cv.imread('tsukuba_gray.png', cv.IMREAD_GRAYSCALE)
image_gamma = gamma_func(image, 2.8)
cv.imwrite('tsukuba_2.8.jpg', image_gamma)
image_gamma = gamma_func(image, 0.5)
cv.imwrite('tsukuba_0.5.jpg', image_gamma)
