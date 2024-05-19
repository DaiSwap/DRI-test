import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_green(image):
    
    blue, green, red = cv2.split(image)

    #histogram
    green_hist = cv2.calcHist([green], [0], None, [256], [0, 256])

    # Plot
    plt.figure()
    plt.plot(green_hist, color='green')
    plt.title('Green Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()

image_path = 'IMG_20230813_131948.jpg'
image = cv2.imread(image_path)

plot_histogram_green(image)