# File: denoising_color.py
# https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html

import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/die.png')
dst = cv.fastNlMeansDenoisingColored(image, dst=None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)

image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
dst_rgb = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

plt.subplot(121), plt.imshow(image_rgb)
plt.subplot(122), plt.imshow(dst_rgb)

plt.show()
