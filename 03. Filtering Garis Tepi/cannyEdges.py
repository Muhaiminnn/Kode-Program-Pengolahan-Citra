import cv2
import numpy as np
from matplotlib import pyplot as plt

# memanggil citra sebagai grayscale (argument 0)
# ubah ‘example_citra.jpg’ dengan nama file Anda
img = cv2.imread('example_citra.jpg',0)
# fungsi Canny Edges dengan argument(img, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
