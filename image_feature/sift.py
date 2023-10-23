# File: sift.py
import cv2 as cv
from print_keypoint import print_keypoint

# image = cv.imread('../images/varese.jpg')
# image = cv.imread('../images/chessboard.png')
image = cv.imread('../images/home.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create(nfeatures=1000)
kp, des = sift.detectAndCompute(gray, mask=None)

print(f'descriptor size: {sift.descriptorSize()}')
print(f'descriptor shape: {des.shape}')
print(f'number of keypoints: {len(kp)}')

for i in range(3):
    print_keypoint(kp[i])

for i in range(3):
    print(des[i])

result_rich = image.copy()
cv.drawKeypoints(gray, keypoints=kp, outImage=result_rich, color=(0, 0, 255),
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('sift-keypoints-rich.jpg', result_rich)

result_simple = image.copy()
cv.drawKeypoints(gray, keypoints=kp, outImage=result_simple, color=(0, 0, 255),
                 flags=cv.DRAW_MATCHES_FLAGS_DEFAULT)
cv.imwrite('sift-keypoints-simple.jpg', result_simple)


cv.imshow('sift keypoints rich', result_rich)
cv.imshow('sift keypoints simple', result_simple)
cv.waitKey()
