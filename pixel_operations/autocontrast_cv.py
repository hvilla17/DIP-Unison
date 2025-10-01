# File: autocontrast_cv.py
# https://github.com/CoinCheung/fixmatch-pytorch/blob/9b5a31d194571fd7d8912032f12a5274d04be814/randaugment.py#L11
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def autocontrast_func(img, cutoff=0):
    # Same output as PIL.ImageOps.autocontrast

    n_bins = 256

    def tune_channel(ch):
        n = ch.size
        cut = cutoff * n // 100
        if cut == 0:
            high, low = ch.max(), ch.min()
        else:
            hist = cv.calcHist([ch], [0], None, [n_bins], [0, n_bins])
            low = np.argwhere(np.cumsum(hist) > cut)
            low = 0 if low.shape[0] == 0 else low[0]
            high = np.argwhere(np.cumsum(hist[::-1]) > cut)
            high = n_bins - 1 if high.shape[0] == 0 else n_bins - 1 - high[0]
        if high <= low:
            table = np.arange(n_bins)
        else:
            scale = (n_bins - 1) / (high - low)
            print(low)
            print(scale)
            offset = -low * scale
            print(offset)
            table = np.arange(n_bins) * scale + offset
            table[table < 0] = 0
            table[table > n_bins - 1] = n_bins - 1
        table = table.clip(0, 255).astype(np.uint8)
        return table[ch]

    channels = [tune_channel(ch) for ch in cv.split(img)]
    out = cv.merge(channels)
    return out


cutoff = 3
image = cv.imread('../images/Alex.jpg', cv.IMREAD_GRAYSCALE)
auto_image = autocontrast_func(image, cutoff=cutoff)

# Display original and corrected image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f'Autocontrast (cutoff={cutoff})')
plt.imshow(auto_image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.tight_layout()
plt.savefig('Alex-autocontrast-cv.png', bbox_inches='tight', pad_inches=0.05)
plt.show()
