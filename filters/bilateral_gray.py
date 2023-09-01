# File: bilateral_gray.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/cameraman.tif')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
patch = gray[35:85, 170:220]
patchVar = np.var(patch)
print(patchVar)

result = cv.bilateralFilter(gray, d=-1, sigmaColor=patchVar, sigmaSpace=2)

cv.imwrite('bilateral-cameraman.tif', result)
