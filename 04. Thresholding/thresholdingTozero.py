import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Baca Citra
img = cv2.imread("example_citra.jpg")

# Proses Thresholding
abu_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
ret, thresholding = cv2.threshold(abu_abu, 127, 255, cv2.THRESH_TOZERO)

# Tampilkan Hasil
plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Citra Asli')

plt.subplot(1, 3, 2)
plt.imshow(abu_abu, cmap = 'gray')
plt.title('Citra Abu-abu')

plt.subplot(1, 3, 3)
plt.imshow(thresholding, cmap = 'gray')
plt.title('Thresholding Biner')

plt.show()
