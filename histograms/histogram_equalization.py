# File: histogram_equalization.py
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/Hawkes_Bay.jpg', cv.IMREAD_GRAYSCALE)

image_equ = cv.equalizeHist(image)

# result = np.hstack((image1, image_equ))  # stacking images side-by-side
# cv.imwrite('Hawkes_Bay_equalized.png', result)

# Display results
plt.figure(figsize=(11, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title('Original Image', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(image_equ, cmap="gray")
plt.title('Equalized Image', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Original Histogram', fontsize=12, weight='bold')
plt.hist(image.ravel(), bins=256, range=(0, 256))

plt.subplot(2, 2, 4)
plt.title('Equalized Histogram', fontsize=12, weight='bold')
plt.hist(image_equ.ravel(), bins=256, range=(0, 256))

plt.tight_layout()
plt.show()
