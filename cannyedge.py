"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('IMG_20230813_140752.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
 
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
plt.show()
"""
import cv2

# Read the input image
image = cv2.imread('IMG_20230813_131943.jpg')

# Define the desired width and height for resizing
desired_width = 1000
desired_height = 800

# Resize the image
resized_image = cv2.resize(image, (desired_width, desired_height))

# Convert the resized image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred_image, 50, 187)  # Adjust threshold values as needed

# Display the original and Canny edge-detected images
cv2.imshow('Original Image', resized_image)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

