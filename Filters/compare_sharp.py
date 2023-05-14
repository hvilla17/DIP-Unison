# File: compare_sharp.py
from laplacian_of_gaussian_sharpening import *
from unsharp_mask import *

image = cv.imread('woman-wearing-red.jpg', cv.IMREAD_COLOR)
log_sharp = laplacian_of_gaussian_sharpening(image, amount=0.7)
usm_sharp = unsharp_mask(image, amount=0.7)
result = np.hstack((log_sharp, usm_sharp))
cv.imwrite('woman-wearing-red-compare.jpg', result)
