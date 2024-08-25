# https://courses.engr.illinois.edu/cs445/fa2023/

import cv2 as cv
import numpy as np


def read_image(image_path):
    intensity_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    return intensity_image.astype(np.float32) / 255
