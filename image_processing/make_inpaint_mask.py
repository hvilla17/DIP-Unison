# File: make_inpaint_mask.py
# https://www.geeksforgeeks.org/image-inpainting-using-opencv/

import cv2 as cv

# reading the damaged image
damaged_img = cv.imread('../images/cat-damaged.png')

# get the shape of the image
height, width = damaged_img.shape[0], damaged_img.shape[1]

# converting all pixels greater than zero to black while black becomes white
for i in range(height):
    for j in range(width):
        if damaged_img[i, j].sum() > 0:
            damaged_img[i, j] = 0
        else:
            damaged_img[i, j] = [255, 255, 255]

# saving the mask
mask = damaged_img
cv.imwrite('cat-damaged-mask.png', mask)

# displaying mask
cv.imshow("damaged image mask", mask)
cv.waitKey(0)
cv.destroyAllWindows()
