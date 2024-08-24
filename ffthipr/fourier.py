# https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.htm

import numpy as np
from operators import log_op
from io_image import read_image
from display import display_image


image_cln = read_image("images/cln1.png")

# Fourier transform
fft_size = 1024  # should be order of 2 (for speed) and include padding
image_fft = np.fft.fft2(image_cln, (fft_size, fft_size))
image_shifted = np.fft.fftshift(image_fft)

# Raw magnitude and phase
image_mag = np.abs(image_shifted)
image_phase = np.angle(image_shifted)
display_image(image_mag, "Magnitude")
display_image(image_phase, "Phase")

# Log magnitude
image_log_mag = log_op(image_mag)
display_image(image_log_mag, "Logarithm magnitude")
