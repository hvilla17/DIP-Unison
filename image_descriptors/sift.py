import cv2 as cv

img = cv.imread('../images/varese.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
key_points, descriptors = sift.detectAndCompute(gray, None)

cv.drawKeypoints(img, key_points, img, (51, 163, 236),
                 cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('sift_key_points', img)
cv.waitKey()
