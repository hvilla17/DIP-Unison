import cv2 as cv

image = cv.imread('../images/cat-face.png')
image_blur = cv.GaussianBlur(image, ksize=(3, 3), sigmaX=0)
image_laplacian = cv.Laplacian(image_blur, ddepth=-1, ksize=3)
image_sharp = image - 0.2 * image_laplacian
cv.imwrite('cat-face-unsharp3.png', image_sharp)
