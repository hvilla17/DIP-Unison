# File: connected_components_plate.py
# https://pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# load the input image from disk, convert it to grayscale, and threshold it
image = cv.imread('../images/Deutschland-license-plate.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
retval, thresh = cv.threshold(gray, thresh=0, maxval=255,
                              type=cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imwrite('Deutschland-thresh.png', thresh)

# apply connected component analysis to the binary image
output = cv.connectedComponentsWithStats(thresh, connectivity=8, ltype=cv.CV_32S)
(numLabels, labels, stats, centroids) = output
print("Number of labels: {}".format(numLabels))

# initialize an output mask to store all characters parsed from the license plate
mask = np.zeros(gray.shape, dtype="uint8")

# loop over the number of unique connected component labels component zero is
# the background
for i in range(1, numLabels):
    # extract the connected component statistics and centroid for the current label
    x = stats[i, cv.CC_STAT_LEFT]
    y = stats[i, cv.CC_STAT_TOP]
    w = stats[i, cv.CC_STAT_WIDTH]
    h = stats[i, cv.CC_STAT_HEIGHT]
    area = stats[i, cv.CC_STAT_AREA]

    # ensure the width, height, and area are all neither too small nor too big
    keepWidth = 100 < w < 300
    keepHeight = 200 < h
    keepArea = 500 < area
    # ensure the connected component we are examining passes all three tests
    if all((keepWidth, keepHeight, keepArea)):
        # construct a mask for the current connected component and
        # then take the bitwise OR with the mask
        print("[INFO] keeping connected component '{}'".format(i))
        print("width: {}, height: {}, area: {}".format(w, h, area))
        componentMask = (labels == i).astype("uint8") * 255
        mask = cv.bitwise_or(mask, componentMask)

cv.imwrite('Deutschland-letters-numbers.png', mask)

# show the original input image and the mask for the license plate characters
plt.figure(1, figsize=(9, 5))
plt.title("Deutsche Kraftfahrzeugkennzeichen")


plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')

plt.subplot(2, 1, 2)
plt.imshow(mask, cmap='gray')

plt.show()
