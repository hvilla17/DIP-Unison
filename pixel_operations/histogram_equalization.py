# File: histogram_equalization.py

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

image = cv.imread('../images/Hawkes_Bay.jpg', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
image_equ = cv.equalizeHist(image)
result = np.hstack((image, image_equ))  # stacking images side-by-side
cv.imwrite('Hawkes_Bay_Equ.png', result)

plot.figure(1)
plot.title("Histograma original")
plot.hist(image.ravel(), 256, (0, 256))
plot.figure(2)
plot.title("Histograma ecualizado")
plot.hist(image_equ.ravel(), 256, (0, 256))
plot.show()
