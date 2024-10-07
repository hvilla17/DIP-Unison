import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load a sample grayscale image (from OpenCV library)
image = cv2.imread("images/lena.jpg", cv2.IMREAD_GRAYSCALE)

# Define a structuring element (3x3 square)
kernel = np.ones((3, 3), np.uint8)

# Apply morphological operations to the grayscale image
# 1. Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# 2. Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# 3. Opening
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# 4. Closing
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 5. Morphological Gradient
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)

# Plotting the results
titles = ['Original Image', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Gradient']
images = [image, erosion, dilation, opening, closing, gradient]

plt.figure(figsize=(12, 8))
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    cv2.imwrite("images_morph/" + titles[i] + ".png", images[i])

plt.tight_layout()
plt.show()
