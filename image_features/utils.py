# https://github.com/spmallick/learnopencv/blob/master/Homography/utils.py

import cv2 as cv
import numpy as np


def mouse_handler(event, x, y, flags, data):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(data['im'], center=(x, y), radius=3, color=(0, 0, 255), thickness=5, lineType=16)
        cv.imshow("Image", data['im'])
        if len(data['points']) < 4:
            data['points'].append([x, y])


def get_four_points(im):
    # Set up data to send to mouse handler
    data = {'im': im.copy(), 'points': []}

    # Set the callback function for any mouse event
    cv.imshow("Image", im)
    cv.setMouseCallback("Image", mouse_handler, data)
    cv.waitKey(0)

    # Convert array to np.array
    points = np.vstack(data['points']).astype(float)

    return points
