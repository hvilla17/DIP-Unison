# File: grabcut.py
import numpy as np
import cv2 as cv

source = cv.imread('../images/statue_small.jpg')
result = source.copy()
mask = np.zeros(result.shape[:2], np.uint8)

background = np.zeros((1, 65), np.float64)
foreground = np.zeros((1, 65), np.float64)

rect = (100, 1, 421, 378)
cv.grabCut(result, mask, rect, background, foreground, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
result = result * mask2[:, :, np.newaxis]

stack_image = np.hstack((source, result))
cv.imwrite('statue_small_grabcut.jpg', stack_image)
