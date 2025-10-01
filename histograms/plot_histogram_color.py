# File: plot_histogram_color.py
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/MyPic.png')

r, g, b = cv.split(image)
for channel, col in zip([r, g, b], ('r', 'g', 'b')):
    hist = cv.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.tight_layout()
plt.show()
