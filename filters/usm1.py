import cv2 as cv

# unsharp mask
image = cv.imread('../images/cat-face.png')
smoothed = cv.GaussianBlur(image, (9, 9), 10)
unsharped = cv.addWeighted(image, 1.5, smoothed, -0.5, 0)
cv.imwrite('cat-face-unsharp1.png', unsharped)
