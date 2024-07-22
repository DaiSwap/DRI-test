import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image = cv2.imread('segmentation\datasets\IMG_20201226_131623.jpg', cv2.IMREAD_GRAYSCALE)

# Apply GaussianBlur to reduce noise and improve edge detection
blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

# Apply the Canny edge detector
edges = cv2.Canny(blurred_image, 100, 200)

# Display the original image and the edges
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')

plt.show()
