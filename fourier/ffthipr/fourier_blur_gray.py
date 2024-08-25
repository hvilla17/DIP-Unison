# https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.htm

import math

import numpy as np

from display import display_image
from io_image import read_image


def dist(_row, _col, _c_row, _c_col):
    d_row = _c_row - _row
    d_col = _c_col - _col
    return math.sqrt(d_row * d_row + d_col * d_col)


r_size = 45
image = read_image("images/stp1.png")

# Fourier transform
image_fft = np.fft.fft2(image)
image_shifted = np.fft.fftshift(image_fft)
num_rows = image_shifted.shape[0]
c_row = (num_rows - 1) // 2
num_cols = image_shifted.shape[1]
c_col = (num_cols - 1) // 2

# Blur
list_res = [[image_shifted[row, col] if dist(row, col, c_row, c_col) <= r_size else 0
             for col in range(num_cols)] for row in range(num_rows)]
result = np.array(list_res)
result_shift = np.fft.ifftshift(result)

# Display
image_blur = np.abs(np.fft.ifft2(result_shift))
image_blur = np.clip(image_blur, a_min=0, a_max=1)
display_image(image, "Original image")
display_image(image_blur, "Blur image")
