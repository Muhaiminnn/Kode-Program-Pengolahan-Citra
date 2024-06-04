import cv2
import matplotlib.pyplot as plt

# Algoritma Haar cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Baca Gambar
img = cv2.imread('foto contoh.jpeg')
abu_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Deteksi wajah
wajah = face_cascade.detectMultiScale(abu_abu, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Memberikan kotak pada wajah
for (x, y, w, h) in wajah:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

# Konversi BGR ke RGB untuk matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Menampilkan Hasil
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(cv2.imread('foto contoh.jpeg'), cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(img_rgb)
plt.title('Wajah Yang Terdeteksi')
plt.axis('off')

plt.show()
