import cv2
import numpy as np

def detect_rectangles(image_path):
    # Read the image
    image = cv2.imread(image_path)
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 80, 100)  # Adjusted edge detection thresholds
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    rectangles = []
    
    # Loop over the contours
    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        # If the contour has 4 vertices, it's likely a rectangle
        if len(approx) == 4:
            rectangles.append(approx)
    
    return rectangles

# Path to the image
image_path = 'imgtest1.jpg'

# Detect rectangles
detected_rectangles = detect_rectangles(image_path)

# Draw rectangles on the image
image_with_rectangles = cv2.imread(image_path)
for rectangle in detected_rectangles:
    cv2.drawContours(image_with_rectangles, [rectangle], -1, (0, 255, 0), 2)

# Show the image with rectangles
cv2.imshow('Detected Rectangles', image_with_rectangles)
cv2.waitKey(0)
cv2.destroyAllWindows()
