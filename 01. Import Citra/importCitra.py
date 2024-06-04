import cv2 # memanggil library OpenCV
from google.colab.patches import cv2_imshow

# sesuaikan dengan nama file
img = cv2.imread("example_citra.jpg")

# menampilkan gambar
cv2_imshow(img)
