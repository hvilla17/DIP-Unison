# File: surf.py

import cv2 as cv

image = cv.imread('../images/home.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(8000)
kp, des = surf.detectAndCompute(gray, None)

cv.drawKeypoints(image, keypoints=kp, outImage=image, color=(51, 163, 236),
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('surf_key_points', image)
cv.waitKey()
