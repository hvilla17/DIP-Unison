# File: display_image_matplot.py
import cv2 as cv
import matplotlib.pyplot as plot

image = cv.imread('../images/MyPic.png')
plot.imshow(image[:, :, ::-1])  # BGR to RGB
plot.show()
