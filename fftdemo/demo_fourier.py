# https://courses.engr.illinois.edu/cs445/fa2023/

from os import path

from display import display_intensity_and_frequency_images
from display import display_intensity_image
from image_processing import fft_image
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

# Visualize FFT magnitudes

# Monaco
display_intensity_image(im_monaco)
display_intensity_and_frequency_images(im_monaco, fft_image(im_monaco))

# Outdoor
display_intensity_image(im_outdoor)
display_intensity_and_frequency_images(im_outdoor, fft_image(im_outdoor))

# Town
display_intensity_image(im_town)
display_intensity_and_frequency_images(im_town, fft_image(im_town))

# Beach
display_intensity_image(im_beach)
display_intensity_and_frequency_images(im_beach, fft_image(im_beach))
