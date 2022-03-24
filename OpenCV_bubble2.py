import numpy as np

import cv2

from matplotlib import pyplot as plt

plt.ion()

filteredContour = []

img = cv2.imread("iiimg/IMG_1673.jpg")

grayImage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

binaryImage = np.uint8((grayImage < 100) *1)

plt.imshow(binaryImage)

