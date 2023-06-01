# File: sobel.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/bikes_gray.jpg')

# directional gradients
grad_x = cv.Sobel(image, ddepth=cv.CV_16S, dx=1, dy=0, ksize=3)
grad_y = cv.Sobel(image, ddepth=cv.CV_16S, dx=0, dy=1, ksize=3)

# scales, calculates absolute values, and converts the result to 8-bit
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)

# gradient
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

result = np.hstack((grad_x, grad_y, grad))
cv.imwrite('bikes_gray_sobel.jpg', result)
