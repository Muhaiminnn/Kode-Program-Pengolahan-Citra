import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

# Baca Citra
img = cv2.imread("example_citra.jpg")

# Grayscale
abu_abu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Proses Blur
blur = cv2.medianBlur(abu_abu, 5)
# Adaptive Thresholding
adaptf_thres = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)#baris ini adalah sambungan dan bukan baris baru

# Tampilkan Hasil
plt.figure(figsize=(10, 3))
plt.imshow(adaptf_thres, cmap = 'gray')
plt.title('Adaptive Thresholding')

plt.show()
