# File: sequence_denoised.py
# https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

handle = cv.VideoCapture('../videos/vtest.avi')

# create a list of first 5 frames
image = [handle.read()[1] for i in range(5)]

# convert all to grayscale
gray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in image]

# convert all to float64
gray = [np.float64(i) for i in gray]

# create a noise of variance 25
noise = np.random.randn(*gray[1].shape) * 5
print(np.var(noise))

# add this noise to images
noisy = [i + noise for i in gray]

# convert back to uint8
noisy = [np.uint8(np.clip(i, a_min=0, a_max=255)) for i in noisy]

# denoise 3rd frame considering all the 5 frames
dst = cv.fastNlMeansDenoisingMulti(noisy, imgToDenoiseIndex=2, temporalWindowSize=5, dst=None, h=4,
                                   templateWindowSize=7, searchWindowSize=35)

# write and display
region_orig = gray[2][0:80, 0:100]
region_noisy = noisy[2][0:80, 0:100]
region_denoised = dst[0:80, 0:100]

cv.imwrite('frame-original.jpg', gray[2])
cv.imwrite('frame-original-region.jpg', region_orig)
cv.imwrite('frame-noisy.jpg', noisy[2])
cv.imwrite('frame-noisy-region.jpg', region_noisy)
cv.imwrite('frame-denoised.jpg', dst)
cv.imwrite('frame-denoised-region.jpg', region_denoised)

plt.subplot(131), plt.imshow(gray[2], cmap='gray')
plt.subplot(132), plt.imshow(noisy[2], cmap='gray')
plt.subplot(133), plt.imshow(dst, cmap='gray')

plt.show()
