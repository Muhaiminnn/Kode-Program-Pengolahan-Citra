import numpy as np
import cv2 
from matplotlib import pyplot as plt

# Baca Citra
img = cv2.imread('example_citra.jpg')

# ORB detector
ORB = cv2.ORB_create()

# kp: variabel untuk menyimpan keypoint yang berhasil dideteksi
kp = ORB.detect(img,None)

# menghitung deskriptor
# kp = keypoints
# des = descriptor
kp, des = ORB.compute(img, kp)

# Jumlah Titik terdeteksi
print("jumlah titik terdeteksi = ", len(kp))

# Menampilkan Keypoint Yang Berhasil Diidentifikasi
img_warna = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.drawKeypoints(img_warna, kp, None, color=(0,255,0), flags=0) # baris ini adalah sambungan
plt.imshow(img2) 
plt.show()
