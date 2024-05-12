import cv2
import numpy as np
import matplotlib.pyplot as plt

def smooth_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

smoothed_image = smooth_image(image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.title('Smoothed')

plt.show()
