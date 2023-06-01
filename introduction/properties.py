# File: properties.py
import cv2 as cv

image = cv.imread('../images/MyPic.png')
print(image.shape)          # (cols, rows, channels)
print(len(image.shape))     # 2 for grayscale; 3 for BGR
print(image.size)           # cols x rows x channels
print(image.dtype)          # generally uint8
