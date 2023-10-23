# File: flann.py
import cv2 as cv
from matplotlib import pyplot as plt

image0 = cv.imread('../images/gauguin_entre_les_lys.jpg', cv.IMREAD_GRAYSCALE)
image1 = cv.imread('../images/gauguin_paintings.png', cv.IMREAD_GRAYSCALE)

# Perform SIFT feature detection and description
sift = cv.SIFT_create()
kp0, des0 = sift.detectAndCompute(image0, mask=None)
kp1, des1 = sift.detectAndCompute(image1, mask=None)
print(len(des0[0]))
print(type(des0))

# Define FLANN-based matching parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Perform FLANN-based matching
flann = cv.FlannBasedMatcher(indexParams=index_params, searchParams=search_params)
matches = flann.knnMatch(queryDescriptors=des0, trainDescriptors=des1, k=2)
print(type(flann))
print(type(matches))
print(matches[0][0].distance)

# Prepare an empty mask to draw good matches
mask_matches = [[0, 0] for i in range(len(matches))]
print(len(matches))
print(range(len(matches)))
print(len(mask_matches))
print(type(mask_matches))

# Populate the mask based on David G. Lowe's ratio test
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7 * n.distance:
        mask_matches[i] = [1, 0]

# Draw the matches that passed the ratio test
img_matches = cv.drawMatchesKnn(img1=image0, keypoints1=kp0,
                                img2=image1, keypoints2=kp1,
                                matches1to2=matches, outImg=None,
                                matchColor=(0, 255, 0), singlePointColor=(255, 0, 0),
                                matchesMask=mask_matches, flags=0)

cv.imwrite('flann-matches.png', img_matches)

# Show the matches
plt.imshow(img_matches)
plt.show()
