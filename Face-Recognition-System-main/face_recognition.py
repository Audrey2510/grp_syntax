from tkinter import *
from tkinter import ttk
import cap as cap
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy
import os
from matplotlib.pyplot import clf


def varchar(param):
    pass


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Taguig City University")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("Sketchy In Snow", 35, "bold"), bg="purple",
                          fg="white")
        title_lbl.place(x=10, y=10, width=1530, height=45)

        # Image in top bar
        img_top = Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\TCUNewLogo.jpg")

        img_top = img_top.resize((700, 650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=700, height=600)

        # Image in side right bar
        img_bottom = Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\aaaaa.jpg")

        img_bottom = img_bottom.resize((600, 650), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=700, y=50, width=600, height=600)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recognition, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="purple", fg="white")
        b1_1.place(x=200, y=550, width=200, height=40)

    # ========Attendance========
    def mark_attendance(self, i, r, n, d):
        with open("MyTest.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # =======face recognition=====
    def face_recognition(self):
        def draw_boundary(img, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="primmie0910",database="tcu_cict_cnn")
                mycursor = conn.cursor()

                # For department fetching
                mycursor.execute("select Student_id from student WHERE Student_id=" + str(id))
                i = mycursor.fetchone()
                i="+".join()

                '''#For course fetching  
                mycursor.execute("select course from student where Student_id="+str(id)) 
                c=mycursor.fetchone() c="+".join(c)

				#For year fetching
				mycursor.execute("select Year from student where Student_id="+str(id)) 
				y=mycursor.fetchone()
				y="+".join(y)

				#For semester fetching
				mycursor.execute("select Semester from student where Student_id="+str(id))
				s=mycursor.fetchone()
				s="+".join(s)
				'''
                # Fetching Name

                mycursor.execute("SELECT Reg FROM student WHERE Student_id=" + str(id))
                r = mycursor.fetchone()
                r="+".join(r)

                # Fetching registration
                mycursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = mycursor.fetchone()
                n="+".join(n)

                # Fetching Student ID
                mycursor.execute("SELECT Dep FROM student WHERE Student_id=" + str(id))
                d = mycursor.fetchone()


                if confidence > 77:
                    cv2.putText(img, f"id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Registration:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(img,f"Semester:{s}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i, r, n, d)

                # If face doesn't match
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, face_cascade):
            coord = draw_boundary(img, 1.1, 10, (255, 25, 255), "Face", clf)

            return img

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


        cap = cv2.VideoCapture(0)  # it was 0 inside

        while True:
            while True:
                # Read the frame
                _, img = cap.read()

                # Convert to grayscale
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # Detect the faces
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)

                # Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), ( 0, 225, 0), 5)

                # Display
                cv2.imshow('Welcome to Face Recognition', img)

                # Stop if escape key is pressed
                k = cv2.waitKey(30) & 0xff
                if k == 27:
                    break


            # Release the VideoCapture object
            cap.release()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
