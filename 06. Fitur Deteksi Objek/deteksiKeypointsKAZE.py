import cv2
import numpy as np

# Baca Citra
img = cv2.imread('example_citra.jpg')

# Citra Keabuan
abu_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# KAZE descriptor
kaze = cv2.KAZE_create()
kp = kaze.detect(abu_abu)

# Computing Descriptors Vector
kp, dsc = kaze.compute(gray, kp)

# Jumlah Titik Yang Terdeteksi
print("jumlah titik terdeteksi = ", len(kp))

# Menampilkan Keypoint Yang Berhasil Diidentifikasi
img_warna = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.drawKeypoints(img_warna, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2) 
plt.show()
