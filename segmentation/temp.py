import cv2 as cv
import numpy as np

print(cv.getNumberOfCPUs())
print(cv.getNumThreads())

image = np.zeros((1000, 1000), dtype=np.uint8)
image[200:800, 200:800] = 255

dist = cv.distanceTransform(image, cv.DIST_L2, 5)
print(np.dtype(dist[0, 0]))
print(dist[500, 500])
cv.imwrite('distance_no_norm.png', dist)

norm=cv.normalize(dist, dst=None, alpha=0.0, beta=255.0, norm_type=cv.NORM_MINMAX)
cv.imwrite('distance_norm_pre.png', norm)
print(np.dtype(norm[0, 0]))
print(norm[500, 500])
result = norm.astype(np.uint8)
cv.imwrite('distance_norm.png', result)
print(np.dtype(result[0, 0]))
print(result[500, 500])
