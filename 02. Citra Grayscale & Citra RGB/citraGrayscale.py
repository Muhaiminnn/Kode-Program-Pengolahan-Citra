import cv2
import matplotlib.pyplot as plt

# Baca citra
img = cv2.imread('example_citra.jpg')

# Ubah citra keabuan
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tampilkan citra asli dan citra keabuan
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Citra Asli')

plt.subplot(1, 2, 2)
plt.imshow(grayscale_img, cmap='gray')
plt.title('Citra Keabuan')
plt.show()
