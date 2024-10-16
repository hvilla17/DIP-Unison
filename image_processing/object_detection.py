# File: object_detection.py
# https://github.com/PyImageSearch/imutils/blob/master/imutils/object_detection.py

# import the necessary packages
import numpy as np


def non_max_suppression(boxes, probs=None, overlap_thresh=0.3):
    # if there are no boxes, return an empty list
    if len(boxes) == 0:
        return []

    # if the bounding boxes are integers, convert them to floats -- this
    # is important since we'll be doing a bunch of divisions
    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    # initialize the list of picked indexes
    pick = []

    # grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    # compute the area of the bounding boxes and grab the indexes to sort
    # (in the case that no probabilities are provided, simply sort on the
    # bottom-left y-coordinate)
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    indexes = y2

    # if probabilities are provided, sort on them instead
    if probs is not None:
        indexes = probs

    # sort the indexes
    indexes = np.argsort(indexes)

    # keep looping while some indexes still remain in the indexes list
    while len(indexes) > 0:
        # grab the last index in the indexes list and add the index value
        # to the list of picked indexes
        last = len(indexes) - 1
        i = indexes[last]
        pick.append(i)

        # find the largest (x, y) coordinates for the start of the bounding
        # box and the smallest (x, y) coordinates for the end of the bounding
        # box
        xx1 = np.maximum(x1[i], x1[indexes[:last]])
        yy1 = np.maximum(y1[i], y1[indexes[:last]])
        xx2 = np.minimum(x2[i], x2[indexes[:last]])
        yy2 = np.minimum(y2[i], y2[indexes[:last]])

        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # compute the ratio of overlap
        overlap = (w * h) / area[indexes[:last]]

        # delete all indexes from the index list that have overlap greater
        # than the provided overlap threshold
        indexes = np.delete(indexes, np.concatenate(([last], np.where(overlap > overlap_thresh)[0])))

    # return only the bounding boxes that were picked
    return boxes[pick].astype("int")
