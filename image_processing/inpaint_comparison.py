# File: inpaint_comparison.py
# https://www.geeksforgeeks.org/image-inpainting-using-opencv/

import cv2 as cv
import numpy as np

# Open the image
image = cv.imread('../images/cat-damaged.png')

# Load the mask
mask = cv.imread('../images/cat-damaged-mask.png', cv.IMREAD_GRAYSCALE)

# Inpaint
dst1 = cv.inpaint(image, mask, inpaintRadius=3, flags=cv.INPAINT_NS)
dst2 = cv.inpaint(image, mask, inpaintRadius=3, flags=cv.INPAINT_TELEA)

# Compare
diff = dst1 - dst2
print('Squared sum: ', np.sum(diff ** 2))
num_zeros = diff.size - np.count_nonzero(diff)
print('Equality index: ', num_zeros / diff.size)

# Write the output
cv.imwrite('cat-inpainted-NS.png', dst1)
cv.imwrite('cat-inpainted-Telea.png', dst2)
