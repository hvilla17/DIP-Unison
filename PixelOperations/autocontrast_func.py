# https://github.com/CoinCheung/fixmatch-pytorch/blob/9b5a31d194571fd7d8912032f12a5274d04be814/randaugment.py#L11

import cv2
import numpy as np


def autocontrast_func(img, cutoff=0):
    # same output as PIL.ImageOps.autocontrast

    n_bins = 256

    def tune_channel(ch):
        n = ch.size
        cut = cutoff * n // 100
        if cut == 0:
            high, low = ch.max(), ch.min()
        else:
            hist = cv2.calcHist([ch], [0], None, [n_bins], [0, n_bins])
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

    channels = [tune_channel(ch) for ch in cv2.split(img)]
    out = cv2.merge(channels)
    return out


image = cv2.imread('Alex.jpg', cv2.IMREAD_GRAYSCALE)
auto_image = autocontrast_func(image, cutoff=3)
cv2.imwrite('Alex_auto.jpg', auto_image)
