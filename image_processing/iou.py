# File: iou.py
# https://learnopencv.com/non-maximum-suppression-theory-and-implementation-in-pytorch/


def iou(x1, y1, a1, b1, x2, y2, a2, b2):
    # find the area for the box1 (x1,y1) (a1,b1)
    area1 = (a1 - x1) * (b1 - y1)

    # find the area for the box2 (x2,y2) (a2,b2)
    area2 = (a2 - x2) * (b2 - y2)

    # Now we need to find the intersection box
    # to do that, find the largest (x, y) coordinates
    # for the start of the intersection bounding box and
    # the smallest (x, y) coordinates for the
    # end of the intersection bounding box
    xx = max(x1, x2)
    yy = max(y1, y2)
    aa = min(a1, a2)
    bb = min(b1, b2)

    # So the intersection BBox has the coordinates (xx,yy) (aa,bb)
    # compute the width and height of the intersection bounding box
    w = max(0, aa - xx)
    h = max(0, bb - yy)

    # find the intersection area
    intersection_area = w * h

    # find the union area of both the boxes
    union_area = area1 + area2 - intersection_area

    # compute the ratio of overlap between the computed
    # bounding box and the bounding box in the area list
    IoU = intersection_area / union_area

    return IoU
