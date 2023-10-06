# File: denoising_color_compare.py
# Based on https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html

import cv2 as cv

image_original = cv.imread('../images/colors-burano.jpg')
image_noisy = cv.imread('../images/colors-burano-noisy.jpg')

dst = cv.fastNlMeansDenoisingColored(image_noisy, dst=None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)
diff = image_original - dst

cv.imwrite('image-denoised.jpg', dst)
cv.imwrite('image-denoised-diff.jpg', diff)
