import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image = cv2.imread('segmentation\datasets\IMG20221119091109.jpg', cv2.IMREAD_GRAYSCALE)

# Apply GaussianBlur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply the Sobel operator in the x direction
sobelx = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)

# Apply the Sobel operator in the y direction
sobely = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the gradient magnitude
sobel_combined = cv2.magnitude(sobelx, sobely)

# Convert the result back to uint8 format
sobel_combined = np.uint8(sobel_combined)

# Display the original image and the Sobel edge detection results
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Sobel X')
plt.imshow(sobelx, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Sobel Y')
plt.imshow(sobely, cmap='gray')

plt.figure()
plt.title('Sobel Combined')
plt.imshow(sobel_combined, cmap='gray')

plt.show()
