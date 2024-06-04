import cv2
import matplotlib.pyplot as plt

# Baca Citra
img = cv2.imread('example_citra.jpg')


# Penskalaan Citra 
skala_citra = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC) # baris ini adalah sambungan dan bukan baris baru

# Tampilkan Hasil
plt.figure(figsize=(10, 3))
plt.subplot(1, 2, 1) 
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')

plt.subplot(1, 2, 2) 
plt.imshow(cv2.cvtColor(skala_citra, cv2.COLOR_BGR2RGB))
plt.title('Setelah Penskalaan')

plt.show()
