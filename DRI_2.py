import cv2
import numpy as np
from skimage.filters import threshold_sauvola

# Preprocess Image with Sauvola Thresholding
def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image to a standard size
    resized_image = cv2.resize(image, (800, 600))
    
    # Apply Sauvola thresholding
    thresh_image = threshold_sauvola(resized_image, window_size=31, k=0.2)
    thresh_image = (resized_image > thresh_image).astype(np.uint8) * 255
    
    return thresh_image

# Load the input image
input_image_path = 'imgtest1.jpg'

# Preprocess the image
preprocessed_image = preprocess_image(input_image_path)

# Display the preprocessed image
cv2.imshow('Preprocessed Image', preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
