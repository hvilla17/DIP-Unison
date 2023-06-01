# https://www.idtools.com.au/unsharp-masking-with-python-and-opencv/
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter

original_image = plt.imread('../images/leuven.jpg').astype('uint16')

# Convert to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Median filtering
gray_image_mf = median_filter(gray_image, 1)

# Calculate the Laplacian
lap = cv2.Laplacian(gray_image_mf, cv2.CV_64F)

# Calculate the sharpened image
sharp = gray_image - 0.7 * lap

cv2.imwrite('leuven-unsharp2.png', sharp)
