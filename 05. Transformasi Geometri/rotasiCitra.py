import cv2
import matplotlib.pyplot as plt
import numpy as np

# Baca Citra
img = cv2.imread('example_citra.jpg')
baris, kolom = img.shape[:2]

# Menentukan titik tengah dan derajat rotasi
Rotasi = cv2.getRotationMatrix2D((kolom/2,baris/2),90, 1)

# Rotasi Citra
rotasi_citra = cv2.warpAffine(img, Rotasi, (kolom, baris)) # baris ini adalah sambungan dan bukan baris baru
# Tampilkan Hasil
plt.figure(figsize=(10, 3))
plt.subplot(1, 2, 1) 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')

plt.subplot(1, 2, 2) 
plt.imshow(cv2.cvtColor(rotasi_citra, cv2.COLOR_BGR2RGB))
plt.title('Setelah Rotasi')

plt.show()
