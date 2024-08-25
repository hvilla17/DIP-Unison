import math

import numpy as np

from display import display_image
from io_image import read_image

'''
    Logarithm Operator
    https://homepages.inf.ed.ac.uk/rbf/HIPR2/pixlog.htm
'''


def log_op(image):
    print("max: ", np.max(image))
    print("min: ", np.min(image))
    # scaling constant for 8 bits
    c = 255.0 / math.log(1 + np.max(image))
    return c * np.log(1 + image)


# test
if __name__ == "__main__":
    image_fce = read_image("images/fce4.png")
    image_man = read_image("images/man8.png")
    image_str = read_image("images/str2.png")
    image_svs = read_image("images/svs1.png")
    image_wom = read_image("images/wom2.png")

    log_fce = log_op(image_fce)
    log_man = log_op(image_man)
    log_str = log_op(image_str)
    log_svs = log_op(image_svs)
    log_wom = log_op(image_wom)

    display_image(log_fce, "fce")
    display_image(log_man, "man")
    display_image(log_str, "str")
    display_image(log_svs, "svs")
    display_image(log_wom, "wom")
