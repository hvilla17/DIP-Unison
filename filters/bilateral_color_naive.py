# File: bilateral_color_naive.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/coloredChips.png')
patch = image[71:127, 34:95]
patchSq = patch ** 2
e_dist = np.sqrt(np.sum(patchSq, 2))
patchVar = np.var(e_dist)
print(patchVar)

result = cv.bilateralFilter(image, d=-1, sigmaColor=patchVar * 2, sigmaSpace=7)

cv.imwrite('bilateral-coloredChips-naive.png', result)
