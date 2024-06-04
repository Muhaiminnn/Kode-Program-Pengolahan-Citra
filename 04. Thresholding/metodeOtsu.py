import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Baca Citra
img = cv2.imread("example_citra.jpg")

# Proses Thresholding
abu_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Proses Blur
blur = cv2.GaussianBlur(abu_abu, (5, 5), 0)

# Thresholding Metode Otsu
ret, otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) # baris ini adalah sambungan dan bukan baris baru

# Tampilkan Hasil
plt.figure(figsize=(10, 3))
plt.imshow(otsu, cmap = 'gray')
plt.title('Metode Otsu')

plt.show()
