# File: orb_match.py
import cv2 as cv
from matplotlib import pyplot as plt

# Load the images
image0 = cv.imread('../images/nasa_logo.png', cv.IMREAD_GRAYSCALE)
image1 = cv.imread('../images/kennedy_space_center.jpg', cv.IMREAD_GRAYSCALE)

# Perform ORB feature detection and description
orb = cv.ORB_create()
kp0, des0 = orb.detectAndCompute(image0, mask=None)
kp1, des1 = orb.detectAndCompute(image1, mask=None)

# Perform brute-force matching
bf = cv.BFMatcher_create(normType=cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(queryDescriptors=des0, trainDescriptors=des1)

# Sort the matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw the best 25 matches
image_matches = cv.drawMatches(img1=image0, keypoints1=kp0,
                               img2=image1, keypoints2=kp1,
                               matches1to2=matches[:25], outImg=None,
                               flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv.imwrite('orb-bf-matches.png', image_matches)

# Show the matches
plt.imshow(image_matches)
plt.show()
