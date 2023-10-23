# File: homography_flann.py

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

MIN_NUM_GOOD_MATCHES = 10

image0 = cv.imread('../images/tattoos/query.png', cv.IMREAD_GRAYSCALE)
image1 = cv.imread('../images/tattoos/anchor-man.png', cv.IMREAD_GRAYSCALE)

# Perform SIFT feature detection and description
sift = cv.SIFT_create()
kp0, des0 = sift.detectAndCompute(image0, mask=None)
kp1, des1 = sift.detectAndCompute(image1, mask=None)

# Define FLANN-based matching parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Perform FLANN-based matching.
flann = cv.FlannBasedMatcher(indexParams=index_params, searchParams=search_params)
matches = flann.knnMatch(queryDescriptors=des0, trainDescriptors=des1, k=2)

# Find all the good matches as per Lowe's ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

if len(good_matches) >= MIN_NUM_GOOD_MATCHES:
    src_pts = np.float32([kp0[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp1[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    M, mask = cv.findHomography(src_pts, dst_pts, method=cv.RANSAC, ransacReprojThreshold=5.0)
    mask_matches = mask.ravel().tolist()

    h, w = image0.shape
    src_corners = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst_corners = cv.perspectiveTransform(src_corners, m=M)
    dst_corners = dst_corners.astype(np.int32)

    # Draw the bounds of the matched region based on the homography
    num_corners = len(dst_corners)
    for i in range(num_corners):
        x0, y0 = dst_corners[i][0]
        if i == num_corners - 1:
            next_i = 0
        else:
            next_i = i + 1
        x1, y1 = dst_corners[next_i][0]
        cv.line(image1, pt1=(x0, y0), pt2=(x1, y1), color=255, thickness=3, lineType=cv.LINE_AA)

    # Draw the matches that passed the ratio test
    img_matches = cv.drawMatches(img1=image0, keypoints1=kp0,
                                 img2=image1, keypoints2=kp1,
                                 matches1to2=good_matches, outImg=None,
                                 matchColor=(0, 255, 0), singlePointColor=None,
                                 matchesMask=mask_matches, flags=2)

    cv.imwrite('homography-result.png', img_matches)

    # Show the homography and good matches
    plt.imshow(img_matches)
    plt.show()
else:
    print("Not enough matches good were found - %d/%d" %
          (len(good_matches), MIN_NUM_GOOD_MATCHES))
