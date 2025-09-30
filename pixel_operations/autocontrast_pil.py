# autocontrast_pil.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

cutoff = 3
image = Image.open('../images/Alex.jpg').convert('L')
print('Original contrast', image.getextrema())
auto_image = ImageOps.autocontrast(image, cutoff=cutoff)
print('Modified contrast', auto_image.getextrema())

# auto_image.save('Alex-autocontrast-pil.png')
# auto_image.show(title='Autocontrast')

# Numpy images
image_original = np.array(image)
image_auto = np.array(auto_image)

# Display original and corrected image_qmark
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title(f'Autocontrast (cutoff={cutoff})')
plt.imshow(auto_image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Original Histogram')
plt.hist(image_original.ravel(), bins=256, range=(0, 256))

plt.subplot(2, 2, 4)
plt.title('Modified Histogram')
plt.hist(image_auto.ravel(), bins=256, range=(0, 256))

plt.tight_layout()
# plt.savefig('Alex-autocontrast-pil.png', bbox_inches='tight', pad_inches=0.05)
plt.show()
