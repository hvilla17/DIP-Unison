# File: bilateral_color.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/coloredChips.png')
lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
patch = lab[71:127, 34:95]
patchSq = patch ** 2
e_dist = np.sqrt(np.sum(patchSq, 2))
patchVar = np.var(e_dist)
print(patchVar)

result = cv.bilateralFilter(lab, d=-1, sigmaColor=patchVar * 2, sigmaSpace=7)

result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
cv.imwrite('bilateral-coloredChips.png', result)
