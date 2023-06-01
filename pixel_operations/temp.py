import cv2 as cv
import numpy as np

image = cv.imread('../images/tsukuba_color.png', cv.IMREAD_GRAYSCALE)
cv.imwrite('tsukuba_gray.png', image)

image = cv.imread('../images/tsukuba_gray.png', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
image_equ = cv.equalizeHist(image)
result = np.hstack((image, image_equ))  # stacking images side-by-side
cv.imwrite('tsukuba_equ.png', result)
