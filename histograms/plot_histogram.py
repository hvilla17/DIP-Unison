# File: plot_normalized.py
import cv2 as cv
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv.imread('../images/Lena_color.png', cv.IMREAD_GRAYSCALE)

# Compute histogram with cv.calcHist
hist = cv.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# Create the histogram figure
plt.figure(figsize=(8, 4))

# Draw histogram as red rectangles
for i, h in enumerate(hist):
    plt.bar(i, h, color='red', width=1)

plt.title('Grayscale Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
