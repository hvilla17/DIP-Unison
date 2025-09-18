# File: multi_template_matching_sk.py
# https://medium.com/towards-artificial-intelligence/introduction-to-image-processing-with-python-3c91dc1e786f

import matplotlib.pyplot as plt
import numpy as np
import skimage as sk

# Read image and convert it to grayscale
# original_image = sk.io.imread('../images/emojis.png')
original_image = sk.io.imread('../images/card_10_hearts.png')
gray_image = sk.color.rgb2gray(original_image[:, :, :3])

# Read the template image
# template = gray_image[1330:1850, 625:1140]
template = sk.io.imread('../images/card_heart.png')
template = sk.color.rgb2gray(template[:, :, :3])

# Perform template matching
result = sk.feature.match_template(gray_image, template)

# Maximum
x, y = np.unravel_index(np.argmax(result), result.shape)
print('Coordinates of the maximum value: ', (x, y))

# Get template size
template_width, template_height = template.shape

# Detect multiple matches above threshold
coords = sk.feature.peak_local_max(result, threshold_abs=0.99)
print('Number of matches detected: ', len(coords))


# Function to draw rectangles on an Axes
def draw_rectangles(ax, coords, w, h, color='red'):
    for x, y in coords:
        rect = plt.Rectangle((y, x), h, w, edgecolor=color, facecolor='none')
        ax.add_patch(rect)


# Display images
fig = plt.figure(figsize=(12, 5))

ax1 = plt.subplot(2, 3, 1)
ax1.imshow(original_image)
ax1.set_title('Original Image', fontsize=20, weight='bold')
ax1.axis('off')

ax2 = plt.subplot(2, 3, 2)
im2 = ax2.imshow(result, cmap='viridis')
ax2.set_title('Result Image', fontsize=20, weight='bold')
fig.colorbar(im2, ax=ax2)
ax2.axis('off')

ax3 = plt.subplot(2, 3, 3)
ax3.imshow(gray_image, cmap='gray')
draw_rectangles(ax3, coords, template_width, template_height)
ax3.set_title('Match in Gray', fontsize=20, weight='bold')
ax3.axis('off')

ax4 = plt.subplot(2, 3, 4)
ax4.imshow(original_image)
draw_rectangles(ax4, coords, template_width, template_height)
ax4.set_title('Match in Color', fontsize=20, weight='bold')
ax4.axis('off')

plt.tight_layout()
plt.show()
