import cv2 as cv

filename = '../images/chessboard.png'
# filename = '../images/chessboard2.jpg'
# filename = '../images/simple.jpg'

img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dst = cv.cornerHarris(gray, 2, 23, 0.04)

# result is dilated for marking the corners, not important
dst = cv.dilate(dst, None)

# threshold for an optimal value, it may vary depending on the image
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('output', dst)
cv.imshow('corners', img)
cv.waitKey()
