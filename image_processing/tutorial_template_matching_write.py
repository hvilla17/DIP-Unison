# File: tutorial_template_matching_write.py
# https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

import cv2 as cv
from matplotlib import pyplot as plot

image = cv.imread('../images/messi5.jpg', cv.IMREAD_GRAYSCALE)
assert image is not None, "file could not be read, check with os.path.exists()"
image2 = image.copy()
template = cv.imread('../images/messi_face.jpg', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
methods = ['cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF']

for m in methods:
    image = image2.copy()
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
    cv.rectangle(image, pt1=top_left, pt2=bottom_right, color=255, thickness=2)

    plot.imshow(result, cmap='gray')
    plot.title('Matching Result'), plot.xticks([]), plot.yticks([])
    plot.show()
    plot.imshow(image, cmap='gray')
    plot.title('Detected Point'), plot.xticks([]), plot.yticks([])
    plot.show()
