# File: multi_template_matching_cv.py
# Based on https://pyimagesearch.com/2021/03/29/multi-template-matching-with-opencv/
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from object_detection import non_max_suppression

threshold = 0.8

# Read image and template
image = cv.imread('../images/card_10_hearts.png')
template = cv.imread('../images/card_heart.png')
# image = cv.imread('../images/emojis.png')
# template = image[1330:1850, 625:1140]

# Convert to RGB
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
template = cv.cvtColor(template, cv.COLOR_RGB2BGR)

(tH, tW) = template.shape[:2]

# Convert image and template to grayscale
image_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
template_gray = cv.cvtColor(template, cv.COLOR_RGB2GRAY)

# Perform template matching
result = cv.matchTemplate(image_gray, template_gray, method=cv.TM_CCOEFF_NORMED)

# Find all locations in the result map where the matched value is
# greater than the threshold, then clone the original image, so we
# can draw on it
(y_coordinates, x_coordinates) = np.where(result >= threshold)
clone = image.copy()
print("[INFO] {} matched locations *before* NMS".format(len(y_coordinates)))

# Loop over starting (x, y)-coordinates
for (x, y) in zip(x_coordinates, y_coordinates):
    # Draw the bounding box on the image
    cv.rectangle(clone, pt1=(x, y), pt2=(x + tW, y + tH), color=(255, 0, 0), thickness=3)

# Show output image *before* applying non-maximum suppression
# cv.imwrite('mtm_cv-before-nms.jpg', clone)


# Initialize list of rectangles
rectangles = []

# Loop over the starting (x, y)-coordinates again
for (x, y) in zip(x_coordinates, y_coordinates):
    # Update the list of rectangles
    rectangles.append((x, y, x + tW, y + tH))

# Apply non-maximum suppression to the rectangles
pick = non_max_suppression(np.array(rectangles))
print("[INFO] {} matched locations *after* NMS".format(len(pick)))

# Loop over the final bounding boxes
for (startX, startY, endX, endY) in pick:
    # Draw the bounding box on the image
    cv.rectangle(image, pt1=(startX, startY), pt2=(endX, endY), color=(255, 0, 0), thickness=3)

# Save the output image
# cv.imwrite('mtm_cv-after-nms.jpg', image)

# Display results
plt.figure(figsize=(11, 5))

plt.subplot(1, 2, 1)
plt.title('Before NMS')
plt.imshow(clone)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('After NMS')
plt.imshow(image)
plt.axis('off')

plt.tight_layout()
plt.show()
