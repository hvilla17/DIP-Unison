# File: hough_circles.py
import cv2 as cv
import numpy as np

image = cv.imread('../images/planet_glow.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_gray = cv.medianBlur(image_gray, 5)
circles = cv.HoughCircles(image_gray, method=cv.HOUGH_GRADIENT, dp=1, minDist=120,
                          param1=100, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)
cv.imwrite('planets_circles.jpg', image)
