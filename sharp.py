import cv2
import numpy as np
import matplotlib.pyplot as plt

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

sharpened_image = sharpen_image(image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(sharpened_image)
plt.title('Sharpened')

plt.show()
