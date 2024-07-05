import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = 'segmentation\simple2.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
"""
# Apply manual thresholding
threshold_value = 190  # Adjust this value based on your needs
_, binary = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Binary Segmentation")
plt.imshow(binary, cmap='gray')
plt.show()
"""

# Apply Otsu's thresholding
_, binary_otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Otsu's Binary Segmentation")
plt.imshow(binary_otsu, cmap='gray')
plt.show()

"""
# Apply adaptive thresholding
binary_adaptive = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 11, 2)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Adaptive Binary Segmentation")
plt.imshow(binary_adaptive, cmap='gray')
plt.show()
"""