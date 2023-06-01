# File: invert_color.py
import cv2 as cv

image = cv.imread('../images/MyPic.png')
image_inv = cv.bitwise_not(image)
cv.imwrite('MyPicInvColor.png', image_inv)
