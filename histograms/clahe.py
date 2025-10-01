# File: clahe.py
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('../images/tsukuba_gray.png', cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
image_clahe = clahe.apply(image)

# Display results
plt.figure(figsize=(11, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(image_clahe, cmap='gray')
plt.title('Equalized Image', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Original Histogram', fontsize=12, weight='bold')
plt.hist(image.ravel(), bins=256, range=(0, 256))

plt.subplot(2, 2, 4)
plt.title('Equalized Histogram', fontsize=12, weight='bold')
plt.hist(image_clahe.ravel(), bins=256, range=(0, 256))

plt.tight_layout()
plt.show()
