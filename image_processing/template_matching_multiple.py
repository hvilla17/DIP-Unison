# File: template_matching_multiple.py
# Based on https://pyimagesearch.com/2021/03/29/multi-template-matching-with-opencv/

import cv2 as cv
import numpy as np

from object_detection import non_max_suppression

threshold = 0.8

# read image and template
image = cv.imread('../images/card_8_diamonds.png')
template = cv.imread('../images/card_diamond.png')
(tH, tW) = template.shape[:2]

# convert image and template to grayscale
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
templateGray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

# perform template matching
result = cv.matchTemplate(imageGray, templateGray, method=cv.TM_CCOEFF_NORMED)

# find all locations in the result map where the matched value is
# greater than the threshold, then clone our original image, so we
# can draw on it
(y_coordinates, x_coordinates) = np.where(result >= threshold)
clone = image.copy()
print("[INFO] {} matched locations *before* NMS".format(len(y_coordinates)))

# loop over our starting (x, y)-coordinates
for (x, y) in zip(x_coordinates, y_coordinates):

    # draw the bounding box on the image
    cv.rectangle(clone, pt1=(x, y), pt2=(x + tW, y + tH),
                 color=(255, 0, 0), thickness=3)

# show our output image *before* applying non-maxima suppression
cv.imshow("Before NMS", clone)
cv.waitKey(0)

# initialize our list of rectangles
rectangles = []

# loop over the starting (x, y)-coordinates again
for (x, y) in zip(x_coordinates, y_coordinates):
    # update our list of rectangles
    rectangles.append((x, y, x + tW, y + tH))

# apply non-maxima suppression to the rectangles
pick = non_max_suppression(np.array(rectangles))
print("[INFO] {} matched locations *after* NMS".format(len(pick)))

# loop over the final bounding boxes
for (startX, startY, endX, endY) in pick:

    # draw the bounding box on the image
    cv.rectangle(image, pt1=(startX, startY), pt2=(endX, endY),
                 color=(255, 0, 0), thickness=3)

# show the output image
cv.imshow("After NMS", image)
cv.waitKey(0)
