# File: fast.py
import cv2 as cv

image = cv.imread('../images/simple.jpg', cv.COLOR_BGR2GRAY)

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()

# Find and draw the keypoints
kp = fast.detect(image, mask=None)
image2 = cv.drawKeypoints(image, keypoints=kp, outImage=None, color=(255, 0, 0))

# Print all default params
print("Threshold: {}".format(fast.getThreshold()))
print("Non max suppression:{}".format(fast.getNonmaxSuppression()))
print("Neighborhood: {}".format(fast.getType()))
print("Total Keypoints with non max suppression: {}".format(len(kp)))

cv.imwrite('fast_true.jpg', image2)

# Disable non max suppression
fast.setNonmaxSuppression(0)
kp = fast.detect(image, mask=None)

print("Total Keypoints without non max suppression: {}".format(len(kp)))
image3 = cv.drawKeypoints(image, keypoints=kp, outImage=None, color=(255, 0, 0))
cv.imwrite('fast_false.jpg', image3)
