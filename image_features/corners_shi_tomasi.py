# File: corners_shi_tomasi.py
import cv2 as cv
import numpy as np

filename = '../images/chessboard.png'
# filename = '../images/chessboard2.jpg'
# filename = '../images/simple.jpg'

image = cv.imread(filename)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
corners = np.intp(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(image, center=(x, y), radius=5, color=(0, 0, 255), thickness=cv.FILLED)

cv.imwrite('corners-shi-tomasi-result.png', image)
