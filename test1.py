import cv2
import numpy as np

# Load the image
image = cv2.imread('imgtest1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area and then remove the largest frame contour
n = len(contours) - 1 
contours = sorted(contours, key=cv2.contourArea, reverse=False)[:n]

# Iterate through contours and draw the largest rectangle surrounding it
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w * h > 100:  # This threshold can be adjusted based on your requirement.
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow('Detected ID Card', image)
cv2.waitKey(0)
