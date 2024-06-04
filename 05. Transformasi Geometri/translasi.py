import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca Citra
img = cv2.imread('example_citra.jpg')
baris, kolom = img.shape[:2]

# Mengatur Pergeseran
pergeserannya = np.float32([
     [1, 0, 100],
     [0, 1, 100]           
    ])
# Translasi Citra
translasi_citra = cv2.warpAffine(img, pergeserannya, (kolom, baris))

# Tampilkan Hasil
plt.figure(figsize=(10, 3))
plt.subplot(1, 2, 1) 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')

plt.subplot(1, 2, 2) 
plt.imshow(cv2.cvtColor(translasi_citra, cv2.COLOR_BGR2RGB))
plt.title('Setelah Translasi')

plt.show()
