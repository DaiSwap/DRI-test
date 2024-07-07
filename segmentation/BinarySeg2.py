import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'segmentation\datasets\simple2.jpg'  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to smooth the image
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply binary thresholding
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Display the original and binary images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Binary Segmentation")
plt.imshow(binary, cmap='gray')
plt.show()

# Save the binary image if needed
# output_path = 'path_to_save_binary_image.jpg'  # Replace with your output path
# cv2.imwrite(output_path, binary)
