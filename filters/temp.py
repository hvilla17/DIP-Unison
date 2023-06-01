import cv2 as cv
import numpy as np

kx, ky = cv.getDerivKernels(dx=2, dy=2, ksize=3, normalize=True)
print(kx)
print('++++++++++')
print(ky)

image = cv.imread('../images/smurf.png')
mask = np.ones((5, 5), np.float32) / 25
print(mask)
result = cv.filter2D(image, ddepth=-1, kernel=mask)
cv.imwrite('smurf-temp.png', result)
