# File: unsharp_mask.py
# https://stackoverflow.com/questions/4993082/how-can-i-sharpen-an-image-in-opencv

import cv2 as cv
import numpy as np


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    # Returns a sharpened version of the image, using an unsharp mask
    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


image = cv.imread('library.jpg')
sharpened_image = unsharp_mask(image, amount=0.5)
result = np.hstack((image, sharpened_image))
cv.imwrite('library_usm.jpg', result)
