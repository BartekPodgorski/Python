import cv2
import matplotlib.pyplot as plt

image = cv2.imread(
    "C:/Users/user/Desktop/Python_Main/Python/obiekt/Film/test_image.jpg")
plt.imshow(image, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])
plt.show()
