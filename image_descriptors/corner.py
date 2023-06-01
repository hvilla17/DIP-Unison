import cv2 as cv

img = cv.imread('../images/chess_board.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dst = cv.cornerHarris(gray, 2, 23, 0.04)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv.imshow('corners', img)
cv.waitKey()
