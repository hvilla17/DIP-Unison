# File: brief_star.py
import cv2 as cv
from print_keypoint import print_keypoint

image = cv.imread('../images/simple.jpg', cv.COLOR_BGR2GRAY)

# Initiate Star detector
star = cv.xfeatures2d.StarDetector_create()

# Initiate BRIEF extractor
brief = cv.xfeatures2d.BriefDescriptorExtractor_create()

# Find the keypoints with STAR
kp = star.detect(image, mask=None)

print(f'number of keypoints: {len(kp)}')

# Compute the descriptors with BRIEF
kp, des = brief.compute(image, keypoints=kp)

print(f'descriptor size: {brief.descriptorSize()}')
print(f'descriptor shape: {des.shape}')
print(f'number of keypoints: {len(kp)}')

for i in range(5):
    print(des[i])

for i in range(3):
    print_keypoint(kp[i])

image2 = cv.drawKeypoints(image, keypoints=kp, outImage=None, color=(255, 0, 0))
cv.imwrite('star.jpg', image2)
