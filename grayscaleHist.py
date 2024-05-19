import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    # grayscale
    gray_image = cv2.imread(image_path, 0)


    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    #plot
    plt.figure()
    plt.title("Grayscale Image Histogram")
    plt.xlabel("range of pixel intensities")
    plt.ylabel("# of Pixels falling in that intensity")
    plt.plot(histogram)
    plt.xlim([0, 256])
    plt.show()

image_path = 'IMG_20230813_131943.jpg'
image = cv2.imread(image_path)

plot_histogram(image)
