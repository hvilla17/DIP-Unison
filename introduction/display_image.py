# File: display_image.py
import cv2 as cv

image = cv.imread('../images/MyPic.png')
cv.imshow('My image', image)
cv.waitKey()
cv.destroyAllWindows()		# destructor de ventanas
