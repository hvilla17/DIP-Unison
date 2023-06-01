# File: hough_lines.py
import cv2 as cv
import numpy as np
import math

image = cv.imread('../images/building.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_edges = cv.Canny(image_gray, threshold1=50, threshold2=200, apertureSize=3)

# copy edges to the images that will display the results in BGR
image_hough_std = cv.cvtColor(image_edges, cv.COLOR_GRAY2BGR)
image_hough_p = np.copy(image_hough_std)

# standard Hough
lines = cv.HoughLines(image_edges, rho=1, theta=np.pi / 180, threshold=180)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
        cv.line(image_hough_std, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

# probabilistic Hough
linesP = cv.HoughLinesP(image_edges, rho=1, theta=np.pi / 180, threshold=80, minLineLength=30, maxLineGap=10)

if linesP is not None:
    for i in range(0, len(linesP)):
        line = linesP[i][0]
        cv.line(image_hough_p, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 3, cv.LINE_AA)

cv.imwrite('building_std.jpg', image_hough_std)
cv.imwrite('building_p.jpg', image_hough_p)
