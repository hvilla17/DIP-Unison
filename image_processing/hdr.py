# https://docs.opencv.org/4.x/d2/df0/tutorial_py_hdr.html

import cv2 as cv
import numpy as np

# Loading exposure images into a list
img_fn = ["images_hdr/img0.jpeg", "images_hdr/img1.jpeg", "images_hdr/img2.jpeg", "images_hdr/img3.jpeg"]
img_list = [cv.imread(fn) for fn in img_fn]
exposure_times = np.array([15.0, 2.5, 0.25, 0.0333], dtype=np.float32)

# Merge exposures to HDR image
merge_debevec = cv.createMergeDebevec()
hdr_debevec = merge_debevec.process(img_list, times=exposure_times.copy())
merge_robertson = cv.createMergeRobertson()
hdr_robertson = merge_robertson.process(img_list, times=exposure_times.copy())

# Tonemap HDR image
tonemap1 = cv.createTonemap(gamma=2.2)
res_debevec = tonemap1.process(hdr_debevec.copy())
tonemap2 = cv.createTonemap(gamma=1.3)
res_robertson = tonemap2.process(hdr_robertson.copy())

# Exposure fusion using Mertens
merge_mertens = cv.createMergeMertens()
res_mertens = merge_mertens.process(img_list)

# Convert datatype to 8-bit and save
res_debevec_8bit = np.clip(res_debevec * 255, 0, 255).astype('uint8')
res_robertson_8bit = np.clip(res_robertson * 255, 0, 255).astype('uint8')
res_mertens_8bit = np.clip(res_mertens * 255, 0, 255).astype('uint8')

cv.imwrite("images_hdr/ldr_debevec.jpg", res_debevec_8bit)
cv.imwrite("images_hdr/ldr_robertson.jpg", res_robertson_8bit)
cv.imwrite("images_hdr/fusion_mertens.jpg", res_mertens_8bit)
