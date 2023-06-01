# File: contour_fish.py
import cv2 as cv
import numpy as np
import random

threshold = 100
image = cv.imread('../images/happy-fish.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_blur = cv.blur(image_gray, (3, 3))
image_canny = cv.Canny(image_blur, threshold, threshold * 2)
# Find contours
contours, hierarchy = cv.findContours(image_canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# Draw contours
drawing = np.zeros((image_canny.shape[0], image_canny.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
cv.imwrite('happy-fish-contours.jpg', drawing)
