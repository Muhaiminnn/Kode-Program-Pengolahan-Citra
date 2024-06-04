import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import kodeTambahan as fr
import csv
from datetime import datetime

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Absensi")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.close)
        self.root.configure(bg="black")

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 720)
        self.cap.set(4, 720)
        self.train_data()
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read('latih111/trainingData.yml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.teks = tk.Label(root, text="Versi 0.0.1", font=("Times New Roman",12), fg="black", bg="black")
        self.teks.grid(row=2, column=1, padx=80, pady=0)
        self.teks = tk.Label(root, text="Versi 0.0.1", font=("Times New Roman",12), fg="black", bg="black")
        self.teks.grid(row=2, column=5, padx=80, pady=0)

        self.judul = tk.Label(root, text="Aplikasi Absen By. Muhaimin", font=("Times New Roman",24), fg="white", bg="black")
        self.judul.grid(row=2, column=2, columnspan=3, padx=5, pady=5)

        self.panel = tk.Label(self.root)
        self.panel.grid(row=3, rowspan=4, column=2, columnspan=3, padx=5, pady=100)

        self.absen_button = tk.Button(root, text="Absen", command=self.absen, width=20, height=3)
        self.absen_button.grid(row=4, column=5, padx=150, pady=5)

        self.sync_button = tk.Button(root, text="Sinkronkan", command=self.train_data, width=20, height=3)
        self.sync_button.grid(row=5, column=5, padx=150, pady=5)

    def train_data(self):
        faces, faceID = fr.labels_for_training_data('111')
        face_recognizer = fr.train_classifier(faces, faceID)
        face_recognizer.write('latih111/trainingData.yml')
        messagebox.showinfo("INFO", "Sinkronisasi Dataset Wajah Berhasil")

    def absen(self):
        name = self.read_name_file()
        retV, test_img = self.cap.read()
        test_img = cv2.flip(test_img, 1)
        faces_detected, gray_img = fr.faceDetection(test_img)
        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y+w, x:x+h]
            label, confidence = self.face_recognizer.predict(roi_gray)
            predicted_name = name[label]
            nama = predicted_name.split("_")[0]
            noid = predicted_name.split("_")[1]
            div = predicted_name.split("_")[2]
        
        with open("daftarHadir.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            lines = list(reader)
            now1 = datetime.now()
            jk = now1.strftime('%H:%M:%S')
            if jk < "17:00:00":
                for line in lines:
                    if line[0] == nama and line[1] == noid and line[2] == div:
                        messagebox.showwarning("INFO", "Anda sudah melakukan absen sebelumnya")
                        return
            elif jk > "17:00:00":
                for line in lines:
                    if line[0] == nama and line[1] == noid and line[2] == div:
                        messagebox.showwarning("INFO", "Anda sudah melakukan absen pulang sebelumnya")
                        return

        with open("daftarHadir.csv",'a', newline='') as f:
            writer = csv.writer(f)
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
           
if dtString < "09:00:00":
                status = "Masuk"
                writer.writerow([nama, noid, div, dtString, status])
                messagebox.showinfo("INFO", "Berhasil Melakukan Absen")
            elif dtString > "17:00:00":
                status = "Pulang"
                writer.writerow([nama, noid, div, dtString, status])
                messagebox.showinfo("INFO", "Absen Pulang Berhasil!")
            else:
                status = "Terlambat"
                writer.writerow([nama, noid, div, dtString, status])
                messagebox.showinfo("INFO", "Anda Terlambat!")

    def read_name_file(self):
        name = {}
        with open("name.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(" :")
                name[int(key)] = value
        return name

    def close(self, event=None):
        self.cap.release()
        cv2.destroyAllWindows()
        self.root.destroy()

    def detect_faces(self):
        name = self.read_name_file()
        retV, test_img = self.cap.read()
        test_img = cv2.flip(test_img, 1)
        faces_detected, gray_img =fr.faceDetection(test_img)
        
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 0, 255), thickness=4)

        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y+w, x:x+h]
            label, confidence=self.face_recognizer.predict(roi_gray)
            fr.draw_rect(test_img, face)
            predicted_name = name[label]
            nama = predicted_name.split("_")[0]
            if confidence < 50:
                fr.put_text(test_img, nama, x + 5, y - 5)
            else:
                predicted_name = name[0]
                fr.put_text(test_img, predicted_name, x + 5, y - 5)

        cv2image = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.panel.imgtk = imgtk
        self.panel.config(image=imgtk)
        self.panel.after(10, self.detect_faces)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    app.detect_faces()
    root.mainloop()
