# File: split.py
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/MyPic.png')

# Writes 3 files, one for each channel
blue = image[:, :, 0]
green = image[:, :, 1]
red = image[:, :, 2]

cv.imwrite('MyPicBlue.jpg', blue)
cv.imwrite('MyPicGreen.jpg', green)
cv.imwrite('MyPicRed.jpg', red)

# Display the RGB channels
fig, ax = plt.subplots(1, 3, figsize=(12, 7))
ax[0].imshow(red, cmap='Reds')
ax[0].set_title('Red')
ax[1].imshow(green, cmap='Greens')
ax[1].set_title('Green')
ax[2].imshow(blue, cmap='Blues')
ax[2].set_title('Blue')
fig.tight_layout()

plt.show()
