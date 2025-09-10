# File: box_filter_rgb.py
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def apply_box_filter_channel(channel, kx=60, ky=60):
    """Apply a box filter in the frequency domain to a single channel."""
    rows, cols = channel.shape
    center_row, center_col = rows // 2, cols // 2

    # FFT + shift
    fft = np.fft.fft2(channel)
    fft_shift = np.fft.fftshift(fft)

    # Create mask
    mask = np.zeros((rows, cols), np.uint8)
    mask[center_row - ky:center_row + ky, center_col - kx:center_col + kx] = 1

    # Apply filter
    fft_shift_filtered = fft_shift * mask

    # Inverse FFT
    fft_inv_shift = np.fft.ifftshift(fft_shift_filtered)
    img_filtered = np.fft.ifft2(fft_inv_shift)
    img_filtered = np.abs(img_filtered)

    return img_filtered, mask


# Read image (color)
image = cv.imread('../images/smurf.png')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # Convert BGR (OpenCV default) → RGB

# Split channels
R, G, B = cv.split(image)
R = R.astype(np.float32) / 255.0
G = G.astype(np.float32) / 255.0
B = B.astype(np.float32) / 255.0

# Apply filters on each channel
kx, ky = 20, 20  # half-width and half-height of box (low-pass region)

R_low, mask_low = apply_box_filter_channel(R, kx, ky)
G_low, _ = apply_box_filter_channel(G, kx, ky)
B_low, _ = apply_box_filter_channel(B, kx, ky)
R_low = np.uint8(np.clip(R_low * 255, 0, 255))
G_low = np.uint8(np.clip(G_low * 255, 0, 255))
B_low = np.uint8(np.clip(B_low * 255, 0, 255))
image_low = cv.merge((R_low, G_low, B_low))

# Save results
temp = cv.cvtColor(image, cv.COLOR_RGB2BGR)
cv.imwrite('xbox_original_color.png', temp)
mask_low = mask_low * 255
cv.imwrite('xbox_mask_color.png', mask_low)
image_low = np.uint8(np.clip(image_low, 0, 255))
temp = cv.cvtColor(image_low, cv.COLOR_RGB2BGR)
cv.imwrite('xbox_image_color.png', temp)

# Display results
plt.figure(figsize=(11, 6))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title(f'Box Mask {2 * kx} x {2 * ky}')
plt.imshow(mask_low, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Low-Pass Filtered')
plt.imshow(image_low)
plt.axis('off')

plt.tight_layout()
plt.show()
