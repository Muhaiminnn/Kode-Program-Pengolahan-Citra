import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

# Baca citra
img = cv2.imread('example_citra.jpg')

# Mengubah warna BGR (OpenCV) menjadi RGB (Matplotlib)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Menampilkan citra dengan Matplotlib
#plt.imshow(img_rgb)
#plt.title('Citra Asli')
#plt.show()

# Memisahkan berdasarkan citra warna
B, G, R = cv2.split(img_rgb)

# Menampilkan setiap citra warna
plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap='Reds')
plt.title('Merah')

plt.subplot(1, 3, 2)
plt.imshow(G, cmap='Greens')
plt.title('Hijau')

plt.subplot(1, 3, 3)
plt.imshow(B, cmap='Blues')
plt.title('Biru')

plt.show()
