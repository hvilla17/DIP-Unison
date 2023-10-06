import cv2 as cv
import numpy as np

image = cv.imread('../images/colors-burano.jpg')

# create noise
noise = np.random.randn(*image.shape) * 10

print(image.shape)
print(noise.shape)
print(np.var(noise))

# add noise
noisy = image + noise

# convert back to uint8
noisy = np.uint8(np.clip(noisy, 0, 255))

diff = image - noisy

cv.imwrite('image-original.jpg', image)
cv.imwrite('image-noisy.jpg', noisy)
cv.imwrite('image-diff.jpg', diff)
