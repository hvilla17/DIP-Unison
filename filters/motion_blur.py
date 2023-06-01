import cv2 as cv
import numpy as np

image = cv.imread('../images/racing-car-1.png')
size = 45

# generating the kernel
mask = np.zeros((size, size))
mask[int((size - 1) / 2), :] = np.ones(size)
mask = mask / size

# applying the kernel to the input image
output = cv.filter2D(image, -1, mask)

result = np.vstack((image, output))
cv.imwrite('racing-car-1-motion-blur.png', result)
