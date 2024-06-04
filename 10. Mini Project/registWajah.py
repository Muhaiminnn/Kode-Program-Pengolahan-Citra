import cv2
import os
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class FaceDataRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Daftar Wajah User")

        self.wajahDir = '111'
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 720)
        self.cam.set(4, 720)
        self.faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')

        self.label = tk.Label(root, text="Daftar Wajah User ke Sistem", font=("Times New Roman",24), width=40, height=1)
        self.label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        self.faceID_label = tk.Label(root, text="ID:", width=15, height=2)
        self.faceID_label.grid(row=1, column=1, padx=5, pady=5)
        self.faceID_entry = tk.Entry(root, width=50)
        self.faceID_entry.grid(row=1, column=2, padx=20, pady=5)
        
        self.nama_label = tk.Label(root, text="Nama:", width=15, height=2)
        self.nama_label.grid(row=2, column=1, padx=5, pady=5)
        self.nama_entry = tk.Entry(root, width=50)
        self.nama_entry.grid(row=2, column=2, padx=20, pady=5)

        self.nim_label = tk.Label(root, text="No. Id:", width=15, height=2)
        self.nim_label.grid(row=3, column=1, padx=5, pady=5)
        self.nim_entry = tk.Entry(root, width=50)
        self.nim_entry.grid(row=3, column=2, padx=20, pady=5)

        self.kelas_label = tk.Label(root, text="Devisi:", width=15, height=2)
        self.kelas_label.grid(row=4, column=1, padx=5, pady=5)
        self.kelas_entry = tk.Entry(root, width=50)
        self.kelas_entry.grid(row=4, column=2, padx=20, pady=5)

        self.daftar_button = tk.Button(root, text="Daftar", command=self.rekam_data, width=15, height=2)
        self.daftar_button.grid(row=1, rowspan=3, column=0,  padx=15, pady=5)

    def rekam_data(self):
        faceID = self.faceID_entry.get()
        nama = self.nama_entry.get()
        nim = self.nim_entry.get()
        kelas = self.kelas_entry.get()

        ambilData = 1
        while True:
            retV, frame = self.cam.read()
            abuabu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.faceDetector.detectMultiScale(abuabu,1.3,5)
            for (x, y, w, h) in faces:
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                x, y, w, h = faces[0]

                # Mengambil crop gambar dari wajah yang terdeteksi
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                face_crop = frame[y:y+h, x:x+w]
                
                gray_frame = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
                namaFile = f"{faceID}_{nama}_{nim}_{kelas}_{ambilData}.jpg"
                cv2.imwrite(os.path.join(self.wajahDir+f'/{faceID}', namaFile), gray_frame)
                if not os.path.exists(self.wajahDir+f'/{faceID}'):
                    os.makedirs(self.wajahDir+f'/{faceID}')
                
                # Menulis data ke file txt untuk identifikasi wajah
                with open("name.txt", "a") as file:
                    file.write(f"{faceID} :{nama}_{nim}_{kelas}\n")
                # menghapus ID duplicate pada file txt
                unique_lines = set()
                with open("name.txt", "r") as file:
                    for line in file:
                        unique_lines.add(line.strip())
                # Menulis kembali baris unik ke file
                with open("name.txt", "w") as file:
                    for line in unique_lines:
                        file.write(f"{line}\n")

                ambilData += 1
                roiabuabu = abuabu[y:y + h, x:x + w]
                roiwarna = frame[y:y + h, x:x + w]
                eyes = self.eyeDetector.detectMultiScale(roiabuabu)
                for (xe, ye, we, he) in eyes:
                    cv2.rectangle(roiwarna, (xe, ye), (xe + we, ye + he), (0, 255, 255), 1)
            cv2.imshow('Daftar Wajah', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  
                break
            elif ambilData > 100:
                break
        messagebox.showinfo("INFO", "Pendaftaran Wajah ke Sistem Berhasil")
        cv2.destroyAllWindows() 
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceDataRecorder(root)
    root.mainloop()
