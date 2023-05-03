# File: display-image.py
import cv2 as cv

image = cv.imread('MyPic.png')
cv.imshow('My image', image)
cv.waitKey()
cv.destroyAllWindows()		# destructor de ventanas
