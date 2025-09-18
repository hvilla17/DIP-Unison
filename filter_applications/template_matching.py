# File: tutorial_template_matching.py
# https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('../images/messi5.jpg', cv.IMREAD_GRAYSCALE)
template = cv.imread('../images/messi_face.jpg', cv.IMREAD_GRAYSCALE)
h, w = template.shape

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for m in methods:
    image2 = image.copy()
    method = eval(m)

    # Apply Template Matching
    result = cv.matchTemplate(image, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(image2, pt1=top_left, pt2=bottom_right, color=255, thickness=2)

    # Display images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(result, cmap='gray')
    plt.title('Matching Result', fontsize=12, weight='bold')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(image2, cmap='gray')
    plt.title('Detected Point', fontsize=12, weight='bold')
    plt.axis('off')

    plt.suptitle(m, fontsize=16, weight='bold')
    plt.show()
