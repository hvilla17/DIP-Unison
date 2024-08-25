# https://towardsdatascience.com/image-processing-with-python-application-of-fourier-transformation-5a8584dc175b

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plot
import math

def dist(_row, _col, _c_row, _c_col):
    d_row = _c_row - _row
    d_col = _c_col - _col
    return math.sqrt(d_row * d_row + d_col * d_col)


image = cv.imread("images/smurf.png")
num_rows = image.shape[0]
c_row = (num_rows - 1) // 2
num_cols = image.shape[1]
c_col = (num_cols - 1) // 2
num_channels = image.shape[2]
font_size = 18
radius = 45
channels = []

for i in range(num_channels):
    rgb_fft = np.fft.fftshift(np.fft.fft2((image[:, :, i])))
    list_res = [[rgb_fft[row, col] if dist(row, col, c_row, c_col) <= radius else 0
                 for col in range(num_cols)] for row in range(num_rows)]
    rgb_blur = np.array(list_res)
    channels.append(abs(np.fft.ifft2(rgb_blur)))

# bgr to rgb
image_final = np.dstack([channels[2].astype(int),
                         channels[1].astype(int),
                         channels[0].astype(int)])

image_final = np.clip(image_final, a_min=0, a_max=255)

fig, ax = plot.subplots(1, 2, figsize=(8, 5))
ax[0].imshow(image[:, :, ::-1])     # bgr to rgb
ax[0].set_title('Original Image', fontsize=font_size)
ax[0].set_axis_off()

ax[1].imshow(image_final)
ax[1].set_title('Transformed Image', fontsize=font_size)
ax[1].set_axis_off()

fig.tight_layout()
plot.show()
