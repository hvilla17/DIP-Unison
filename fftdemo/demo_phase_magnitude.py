# https://courses.engr.illinois.edu/cs445/fa2023/

from os import path

import matplotlib.pyplot as plt

from display import merge_and_display_mag_phase, display_mag_phase_images
from image_processing import get_mag_phase_images
from io_image import read_image

# Load in images
image_path = './data'

# List all image names
im_beach_filename = 'im_beach.JPG'
im_monaco_filename = 'im_monaco.png'
im_outdoor_filename = 'im_outdoor.png'
im_town_filename = 'im_town.png'

# Setup full path
im_beach_file = path.join(image_path, im_beach_filename)
im_monaco_file = path.join(image_path, im_monaco_filename)
im_outdoor_file = path.join(image_path, im_outdoor_filename)
im_town_file = path.join(image_path, im_town_filename)

# Read files in grayscale, and convert to float
im_beach = read_image(im_beach_file)
im_monaco = read_image(im_monaco_file)
im_outdoor = read_image(im_outdoor_file)
im_town = read_image(im_town_file)

# Compute FFT magnitude and phases

# Run FFT to obtain real and imaginary frequencies.
# Then compute magnitude and phase of transformed values.
images = get_mag_phase_images(im_outdoor, im_monaco)
im1, im1_mag, im1_phase, im2, im2_mag, im2_phase = images

# Let's display them.
display_mag_phase_images(*images)

# Merge magnitude and phase of different images

# First merge magnitude of image 1, and phase of image 2.
im1_mag_im2_phase = merge_and_display_mag_phase(im2, im1_mag, im2_phase)

# Now, let's merge magnitude of image 2, and phase of image 1
im2_mag_im1_phase = merge_and_display_mag_phase(im2, im2_mag, im1_phase)

# Visualize it
fig, axes = plt.subplots(2, 2, figsize=(10, 13))
[a.axis('off') for a in axes.ravel()]
axes[0, 0].imshow(images[0], cmap='gray')
axes[0, 1].imshow(images[3], cmap='gray')
axes[1, 0].imshow(im2_mag_im1_phase, cmap='gray')
axes[1, 1].imshow(im1_mag_im2_phase, cmap='gray')
axes[0, 0].set_title('Image 1')
axes[0, 1].set_title('Image 2')
axes[1, 0].set_title('Image 2 Mag + Image 1 Phase')
axes[1, 1].set_title('Image 1 Mag + Image 2 Phase')
plt.show()
