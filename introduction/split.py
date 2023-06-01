# File: split.py
import cv2 as cv

image = cv.imread('../images/MyPic.png')

# Writes 3 files, one for each channel
blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

cv.imwrite('MyPicBlue.jpg', blue)
cv.imwrite('MyPicGreen.jpg', green)
cv.imwrite('MyPicRed.jpg', red)
