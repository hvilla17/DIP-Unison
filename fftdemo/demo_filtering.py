# https://courses.engr.illinois.edu/cs445/fa2023/

from os import path

from display import display_filtering_process
from io_image import read_image
from kernels import gaussian_kernel2d, box_kernel2d, sobel_kernel2d, log_kernel2d

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

# Create filters
gaussian_filter = gaussian_kernel2d(31, 4)
sobel_filter = sobel_kernel2d()
log_filter = log_kernel2d(31, 4)
box_filter = box_kernel2d(31, 4)

# Display filtering processes

# Sobel filter
images_sobel = display_filtering_process(im_town, sobel_filter)

# Gaussian filter
images_gaussian = display_filtering_process(im_town, gaussian_filter)

# Log filter
images_log = display_filtering_process(im_town, log_filter)

# Box filter
images_box = display_filtering_process(im_town, box_filter)
