import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram_blue(image):
    
    blue, green, red = cv2.split(image)

    #histogram
    blue_hist = cv2.calcHist([blue], [0], None, [256], [0, 256])

    # Plot
    plt.figure()
    plt.plot(blue_hist, color='blue')
    plt.title('Blue Channel Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.xlim([0, 256])
    plt.show()

image_path = 'IMG_20230813_131948.jpg'
image = cv2.imread(image_path)

plot_histogram_blue(image)
