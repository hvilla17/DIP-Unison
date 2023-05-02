# File: threshold.py
import cv2 as cv

image = cv.imread('MyPic.png')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# above 150 to white; 150 and below to black
_, dst = cv.threshold(image_gray, 150, 255, cv.THRESH_BINARY)
cv.imwrite('MyPicBW.png', dst)
