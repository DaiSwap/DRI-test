import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image_path = 'segmentation/datasets/simple2.jpg'  # Replace with your image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Plot the histogram of the image
plt.figure(figsize=(10, 5))
plt.hist(image.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
plt.title('Histogram of Pixel Intensities')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
