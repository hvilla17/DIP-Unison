# File: test_noise.py
# Load image
import cv2 as cv
import matplotlib.pyplot as plt

from add_noise import *

image = cv.imread('../images/Lena.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# Normalize between 0 and 1
image_float = image.astype(np.float32) / 255.0

# Apply noise
gaussian_noisy = add_gaussian_noise(image_float, mean=0, sigma=0.1)
gaussian_noisy = np.uint8(gaussian_noisy * 255)
sp_noisy = add_salt_and_pepper_noise(image_float, salt_prob=0.02, pepper_prob=0.05)
sp_noisy = np.uint8(sp_noisy * 255)

# Show results
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))

axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(gaussian_noisy)
axes[1].set_title('Gaussian Noise')
axes[1].axis('off')

axes[2].imshow(sp_noisy)
axes[2].set_title('Salt & Pepper Noise')
axes[2].axis('off')

plt.tight_layout()
plt.show()
