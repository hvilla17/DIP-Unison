import os

import numpy as np
import cv2 as cv


def create_descriptors(folder):
    feature_detector = cv.SIFT_create()
    files = []
    for (dir_path, dir_names, filenames) in os.walk(folder):
        files.extend(filenames)
    for f in files:
        create_descriptor(folder, f, feature_detector)


def create_descriptor(folder, image_path, feature_detector):
    if not image_path.endswith('png'):
        print('skipping %s' % image_path)
        return
    print('reading %s' % image_path)
    img = cv.imread(os.path.join(folder, image_path),
                    cv.IMREAD_GRAYSCALE)
    key_points, descriptors = feature_detector.detectAndCompute(
        img, None)
    descriptor_file = image_path.replace('png', 'npy')
    np.save(os.path.join(folder, descriptor_file), descriptors)


directory = '../images/tattoos'
create_descriptors(directory)
