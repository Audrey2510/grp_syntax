from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Developer:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")



		title_lbl=Label(self.root,text="About TCU",font=("Sketchy In Snow", 35,"bold"),bg="red",fg="white")
		title_lbl.place(x=0,y=0,width=1530,height=45)

		#Image in top bar
		img_top=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\TCUNewLogo-removebg-preview.png")
		
		img_top=img_top.resize((1000,1000),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		f_lbl=Label(self.root,image=self.photoimg_top)
		f_lbl.place(x=25,y=55,width=1330,height=720)



		#Frame
		main_frame=Frame(f_lbl,bd=2,bg="white")
		main_frame.place(x=800,y=0,width=500,height=600)



		#Developer Info
		def callback(url):
			webbrowser.open_new(url)
		dev_label=Label(main_frame,text="Taguig City University (TCU) is a Philippine local \nuniversity.It was established in 2006 by the Sangguniang \nBayan of the Municipal Government of Taguig\nIt is located in Gen. Santos Ave., Central Bicutan, \nTaguig City.",font=("times new roman",10,"bold"),bg="white")
		dev_label.place(x=0,y=110)


		dev_label = Label(main_frame, text="Mission",
						  font=("times new roman", 15, "bold"), bg="white")
		dev_label.place(x=0, y=210)

		dev_label = Label(main_frame, text="To Nurture a vibrant culture \nAcademic wellness responsive to\n The challenges of technology\nand the global community",
						  font=("times new roman", 10, "bold"), bg="white")
		dev_label.place(x=0, y=240)

		dev_label = Label(main_frame, text="Vision", font=("times new roman", 15, "bold"), bg="white")
		dev_label.place(x=20, y=310)

		dev_label = Label(main_frame, text="An eminent center of excellent\nHigher Education towards\nSocietal advancement", font=("times new roman", 10, "bold"), bg="white")
		dev_label.place(x=0, y=340)

		dev_label = Label(main_frame, text="Philosophy", font=("times new roman", 15, "bold"), bg="white")
		dev_label.place(x=0, y=410)

		dev_label = Label(main_frame, text="Societal transformation\nFor a caring community\nAnd an ecologically\nBalanced country", font=("times new roman", 10, "bold"), bg="white")
		dev_label.place(x=0, y=440)

		dev_label1=Label(main_frame,text="Our Website: Taguig City University", fg="blue", cursor="hand2")
		dev_label1.place(x=0,y=400)
		dev_label1.pack()
		dev_label1.bind("<Button-1>", lambda e: callback("https://tcu.taguig.gov.ph/"))

		
		dev_label2=Label(main_frame,text="Our Facebook Page: Taguig City University 2022", fg="blue", cursor="hand2")
		dev_label2.place(x=0,y=150)
		dev_label2.pack()
		dev_label2.bind("<Button-1>", lambda e: callback("https://www.facebook.com/TCUOfficial2022"))





if __name__=="__main__":
	root=Tk()
	obj=Developer(root)
	root.mainloop()			