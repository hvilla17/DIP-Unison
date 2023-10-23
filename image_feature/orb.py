# File: orb.py
import cv2 as cv
from print_keypoint import print_keypoint

image = cv.imread('../images/home.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

orb = cv.ORB_create(nfeatures=10000, scaleFactor=2.0)
kp, des = orb.detectAndCompute(gray, mask=None)

cv.imwrite('orb-gray.jpg', gray)

print(f'descriptor size: {orb.descriptorSize()}')
print(f'descriptor shape: {des.shape}')
print(f'number of keypoints: {len(kp)}')

for i in range(3):
    print_keypoint(kp[i])

for i in range(3):
    print(des[i])

result_rich = image.copy()
cv.drawKeypoints(gray, keypoints=kp, outImage=result_rich, color=(0, 0, 255),
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imwrite('orb-keypoints-rich.jpg', result_rich)

result_simple = image.copy()
cv.drawKeypoints(gray, keypoints=kp, outImage=result_simple, color=(0, 0, 255),
                 flags=cv.DRAW_MATCHES_FLAGS_DEFAULT)
cv.imwrite('orb-keypoints-simple.jpg', result_simple)

cv.imshow('orb keypoints rich', result_rich)
cv.imshow('orb keypoints simple', result_simple)
cv.waitKey()
