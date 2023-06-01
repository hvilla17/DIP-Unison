import cv2 as cv
from matplotlib import pyplot as plt

# Load the images.
img0 = cv.imread('../images/nasa_logo.png',
                  cv.IMREAD_GRAYSCALE)
img1 = cv.imread('../images/kennedy_space_center.jpg',
                  cv.IMREAD_GRAYSCALE)

# Perform ORB feature detection and description.
orb = cv.ORB_create()
kp0, des0 = orb.detectAndCompute(img0, None)
kp1, des1 = orb.detectAndCompute(img1, None)

# Perform brute-force matching.
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des0, des1)

# Sort the matches by distance.
matches = sorted(matches, key=lambda x:x.distance)

# Draw the best 25 matches.
img_matches = cv.drawMatches(
    img0, kp0, img1, kp1, matches[:25], img1,
    flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# Show the matches.
plt.imshow(img_matches)
plt.show()
