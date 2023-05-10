# File: image_intensity.py
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plot

image = cv.imread('MyPic.png')

# Plot the original image
plot.subplot(1, 2, 1)
plot.title("Original")
plot.imshow(image[:, :, ::-1])

# Adjust the brightness and contrast
brightness = 10  # adds 10 to each pixel value
contrast = 2.3  # scales the pixel values by 2.3
image2 = cv.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

cv.imwrite('modified_image.jpg', image2)  # Save the image

# Plot the contrast image
plot.subplot(1, 2, 2)
plot.title("Brightness & contrast")
plot.imshow(image2[:, :, ::-1])
plot.show()
