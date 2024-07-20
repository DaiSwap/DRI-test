import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = 'segmentation\datasets\road1.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, binary_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Invert the binary image to switch foreground and background
binary_inverted = cv2.bitwise_not(binary_otsu)

# Display the original, Otsu thresholded, and inverted binary images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title("Otsu's Binary Segmentation")
plt.imshow(binary_otsu, cmap='gray')

plt.subplot(1, 3, 3)
plt.title("Inverted Binary Segmentation")
plt.imshow(binary_inverted, cmap='gray')

plt.show()

