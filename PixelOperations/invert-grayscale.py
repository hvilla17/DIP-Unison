# File: invert-grayscale.py
import cv2 as cv

image = cv.imread('MyPic.png', cv.IMREAD_GRAYSCALE)
image_inv = cv.bitwise_not(image)
cv.imwrite('MyPicInvGray.png', image_inv)
