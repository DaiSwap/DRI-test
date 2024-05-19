import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_bgr(image):
    blue, green, red = cv2.split(image)

    # histograms
    blue_hist = cv2.calcHist([blue], [0], None, [256], [0, 256])
    #green_hist = cv2.calcHist([green], [0], None, [256], [0, 256])
    #red_hist = cv2.calcHist([red], [0], None, [256], [0, 256])

    # Plot 
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(blue_hist, color='blue')
    plt.title('Blue Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
"""
    plt.subplot(3, 1, 2)
    plt.plot(green_hist, color='green')
    plt.title('Green Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 3)
    plt.plot(red_hist, color='red')
    plt.title('Red Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
"""
plt.tight_layout()
plt.show()

image_path = 'IMG_20230813_130433.jpg'
image = cv2.imread(image_path)

plot_histogram_bgr(image)
