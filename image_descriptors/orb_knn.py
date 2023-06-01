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

# Perform brute-force KNN matching.
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=False)
pairs_of_matches = bf.knnMatch(des0, des1, k=2)

# Sort the pairs of matches by distance.
pairs_of_matches = sorted(pairs_of_matches, key=lambda x: x[0].distance)

# Draw the 25 best pairs of matches.
img_pairs_of_matches = cv.drawMatchesKnn(
    img0, kp0, img1, kp1, pairs_of_matches[:25], img1,
    flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# Show the pairs of matches.
plt.imshow(img_pairs_of_matches)
plt.show()

# Apply the ratio test.
matches = [x[0] for x in pairs_of_matches
           if len(x) > 1 and x[0].distance < 0.8 * x[1].distance]

# Draw the best 25 matches.
img_matches = cv.drawMatches(
    img0, kp0, img1, kp1, matches[:25], img1,
    flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# Show the matches.
plt.imshow(img_matches)
plt.show()
