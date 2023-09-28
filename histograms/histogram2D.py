# File: histogram2D.py
import cv2 as cv
from matplotlib import pyplot as plot

image = cv.imread('../images/sea-fish.jpg')
hist = cv.calcHist([image], channels=[0, 1], mask=None, histSize=[256, 256],
                   ranges=[0, 256, 0, 256])
hist = cv.normalize(hist, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
hist = 255 - hist

image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
hist_hsv = cv.calcHist([image_hsv], channels=[0, 1], mask=None, histSize=[180, 256],
                       ranges=[0, 180, 0, 256])
hist_hsv = cv.normalize(hist_hsv, dst=None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX)
hist_hsv = 255 - hist_hsv

plot.figure()
plot.xlabel('Blue', fontweight='bold')
plot.ylabel('Green', fontweight='bold')
plot.title('Blue vs Green')
plot.imshow(hist, cmap='gray', interpolation='nearest')

plot.figure()
plot.xlabel('Saturation', fontweight='bold')
plot.ylabel('Hue', fontweight='bold')
plot.title('Hue vs Saturation')
plot.imshow(hist_hsv, cmap='gray', interpolation='nearest')

plot.show()
