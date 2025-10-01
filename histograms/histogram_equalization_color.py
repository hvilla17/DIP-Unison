# File: histogram_equalization_color.py
import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('../images/9.bmp')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Equalize each RGB channel
r, g, b = cv.split(image)
equ_r = cv.equalizeHist(r)
equ_g = cv.equalizeHist(g)
equ_b = cv.equalizeHist(b)
image_eq_rgb = cv.merge((equ_r, equ_g, equ_b))

# Convert the RGB image to YUV format
image_yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)

# Equalize the histogram of the Y channel
image_yuv[:, :, 0] = cv.equalizeHist(image_yuv[:, :, 0])

# Convert the YUV image back to RGB format
image_eq_yuv = cv.cvtColor(image_yuv, cv.COLOR_YUV2RGB)

# Display results
plt.figure(figsize=(11, 5))

plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title('Original Image', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(image_eq_rgb)
plt.title('Equalization RGB', fontsize=12, weight='bold')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Equalization YUV', fontsize=12, weight='bold')
plt.imshow(image_eq_yuv)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title('Original Histogram', fontsize=12, weight='bold')
r, g, b = cv.split(image)
for channel, col in zip([r, g, b], ('r', 'g', 'b')):
    histr = cv.calcHist(images=[channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.subplot(2, 3, 5)
plt.title('Equalized Histogram RGB', fontsize=12, weight='bold')
r, g, b = cv.split(image)
for channel, col in zip([r, g, b], ('r', 'g', 'b')):
    histr = cv.calcHist(images=[channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.subplot(2, 3, 6)
plt.title('Equalized Histogram YUV', fontsize=12, weight='bold')
r, g, b = cv.split(image)
for channel, col in zip([r, g, b], ('r', 'g', 'b')):
    histr = cv.calcHist(images=[channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

plt.tight_layout()
plt.show()
