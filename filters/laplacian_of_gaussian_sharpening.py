# File: laplacian_of_gaussian_sharpening.py
import cv2 as cv
import numpy as np


def laplacian_of_gaussian_sharpening(source, amount=0.5):
    # Returns a sharpened version of the image, using the laplacian of the gaussian
    _smooth = cv.GaussianBlur(source, ksize=(3, 3), sigmaX=0)
    # since the input is CV_8U, ddepth is CV_16S to avoid overflow
    _laplacian = cv.Laplacian(_smooth, ddepth=cv.CV_16S, ksize=3)
    # converting back to uint8
    _laplacian = cv.convertScaleAbs(_laplacian)
    _sharp = source - amount * _laplacian
    return _sharp


image = cv.imread('../images/library.jpg', cv.IMREAD_COLOR)
sharp = laplacian_of_gaussian_sharpening(image, amount=0.2)
result = np.hstack((image, sharp))
cv.imwrite('library_sharp_log.jpg', result)
