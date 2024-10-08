# File: connected_components_all.py
# https://pyimagesearch.com/2021/02/22/opencv-connected-component-labeling-and-analysis/

import cv2 as cv
import matplotlib.pyplot as plt

# filename = '../images/Deutschland-license-plate.png'
filename = '../images/tools.png'

# load the input image from disk, convert it to grayscale, and
# threshold it
image = cv.imread(filename)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
retval, thresh = cv.threshold(gray, 0, 255,
                              cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

# apply connected component analysis to the binary image
output = cv.connectedComponentsWithStats(thresh, connectivity=8, ltype=cv.CV_32S)
(numLabels, labels, stats, centroids) = output
print("Number of labels: {}".format(numLabels))
print(labels.shape)
print(type(labels))

# loop over the number of unique connected component labels
output = image.copy()
for i in range(0, numLabels):
    # if this is the first component then we examine the
    # *background* (typically we would just ignore this
    # component in our loop)
    if i == 0:
        text = "examining component {}/{} (background)".format(i + 1, numLabels)
    # otherwise, we are examining an actual connected component
    else:
        text = "examining component {}/{}".format(i + 1, numLabels)

    # print a status message update for the current connected
    # component
    print("[INFO] {}".format(text))

    # extract the connected component statistics and centroid for
    # the current label
    x = stats[i, cv.CC_STAT_LEFT]
    y = stats[i, cv.CC_STAT_TOP]
    w = stats[i, cv.CC_STAT_WIDTH]
    h = stats[i, cv.CC_STAT_HEIGHT]
    area = stats[i, cv.CC_STAT_AREA]
    (cX, cY) = centroids[i]
    print("Position: ", (x, y, w, h))
    print("Area: ", area)
    print("Centroid: ", (cX, cY))

    # clone our original image (so we can draw on it) and then draw
    # a bounding box surrounding the connected component along with
    # a circle corresponding to the centroid
    cv.rectangle(output, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 0), 3)
    cv.circle(output, (int(cX), int(cY)), 4, (0, 0, 255), -1)

# show our output image
plt.figure(1, figsize=(9, 5))
plt.imshow(output, cmap='gray')
plt.show()
