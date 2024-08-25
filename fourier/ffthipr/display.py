# https://courses.engr.illinois.edu/cs445/fa2023/

import matplotlib.pyplot as plot

def display_image(image, title):
    fig = plot.figure(figsize=(7.5, 5))
    plot.title(title)
    plot.imshow(image, cmap='gray')
    plot.axis('off')
    plot.show()
