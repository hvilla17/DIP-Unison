import cv2 as cv

img = cv.imread('../images/varese.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(8000)
key_points, descriptors = surf.detectAndCompute(gray, None)

cv.drawKeypoints(img, key_points, img, (51, 163, 236),
                  cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('surf_key_points', img)
cv.waitKey()
