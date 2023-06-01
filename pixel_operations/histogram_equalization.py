# File: histogram_equalization.py

import cv2 as cv
import numpy as np

image = cv.imread('../images/Hawkes_Bay.jpg', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
image_equ = cv.equalizeHist(image)
result = np.hstack((image, image_equ))  # stacking images side-by-side
cv.imwrite('Hawkes_Bay_Equ.png', result)
