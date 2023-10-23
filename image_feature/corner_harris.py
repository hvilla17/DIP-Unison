# File: corner_harris.py
import cv2 as cv

filename = '../images/chessboard.png'
# filename = '../images/chessboard2.jpg'
# filename = '../images/simple.jpg'

image = cv.imread(filename)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
dst = cv.cornerHarris(gray, blockSize=2, ksize=23, k=0.04)

# result is dilated for marking the corners, not important
dst = cv.dilate(dst, None)

# threshold for an optimal value, it may vary depending on the image
image[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imwrite('corners-harris-output.png', dst)
cv.imwrite('corners-harris-result.png', image)

cv.imshow('output', dst)
cv.imshow('corners', image)
cv.waitKey()
