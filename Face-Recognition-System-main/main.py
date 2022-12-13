from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime 
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpdesk import Help
import tkinter
from chatbot import ChatBot


class Face_Recognition_System:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")

    #background image=======
		img3=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\tcu_cict_cnn.webp")
		
		img3=img3.resize((600,500),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=-700,y=50,width=2000,height=625)


		#===========Time========




	#student button====
		img4=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\download.jfif")
		
		img4=img4.resize((150,125),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		b1=Button(bg_img,image=self.photoimg4, command=self.student_details,cursor="hand2")
		b1.place(x=1350,y=0,width=150,height=125)

		b1_1=Button(bg_img,text="Student Details", command=self.student_details,cursor="hand2",font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1350,y=120,width=150,height=40)

	#face detection button====
		img5=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\Facial recognition glyph icon.jfif")
		
		img5=img5.resize((150,125),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		b1=Button(bg_img,image=self.photoimg5,cursor="hand2", command=self.face_data)
		b1.place(x=1550,y=0,width=150,height=125)

		b1_1=Button(bg_img,text="Face Detector ",cursor="hand2",command=self.face_data,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1550,y=120,width=150,height=40)

	#Attendance detection button====
		img6=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\Attendance presence icon.jfif")
		
		img6=img6.resize((150,125),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
		b1.place(x=1750,y=0,width=150,height=125)

		b1_1=Button(bg_img,text="Attendance ",cursor="hand2",command=self.attendance_data,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1750,y=120,width=150,height=40)

	#Chat button====
		img7=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\Chatbot message glyph icon.jfif")
		
		img7=img7.resize((150,125),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		b1=Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.chatbot)
		b1.place(x=1350,y=200,width=150,height=125)

		b1_1=Button(bg_img,text="Chat Bot ",cursor="hand2",command=self.chatbot,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1350,y=325,width=150,height=40)

	#Train button====
		img8=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\Iconos gratuitos de Documento diseñados por flatart_icons.png")
		
		img8=img8.resize((200,150),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		b1=Button(bg_img,image=self.photoimg8,cursor="hand2", command=self.train_data)
		b1.place(x=1550,y=200,width=150,height=125)

		b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1550,y=325,width=150,height=40)

	#Photos button====
		img9=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\ff.jfif")
		
		img9=img9.resize((150,125),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		b1=Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.open_img)
		b1.place(x=1750,y=200,width=150,height=125)

		b1_1=Button(bg_img,text="Photos",cursor="hand2", command=self.open_img, font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1750,y=325,width=150,height=40)

	#Developer button====
		img10=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\TCUNewLogo.jpg")
		
		img10=img10.resize((150,125),Image.ANTIALIAS)
		self.photoimg10=ImageTk.PhotoImage(img10)

		b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
		b1.place(x=1450,y=400,width=150,height=125)

		b1_1=Button(bg_img,text="ABOUT TCU",cursor="hand2",command=self.developer_data,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1450,y=525,width=150,height=40)

	#Exit button====
		img11=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\Exit Silhouette PNG Transparent, Exit Icon, Exit Icons, Exit, Leave PNG Image For Free Download.png")
		
		img11=img11.resize((150,125),Image.ANTIALIAS)
		self.photoimg11=ImageTk.PhotoImage(img11)

		b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
		b1.place(x=1650,y=400,width=150,height=125)

		b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Sketchy In Snow", 15,"bold"),bg="purple",fg="white")
		b1_1.place(x=1650,y=525,width=150,height=40)

	# Opening image function in photos section
	
	def open_img(self):
		os.startfile("data")

	#Exit func
	def iExit(self):
		self.iExit=tkinter.messagebox.askyesno("Face Recongnition","Are you sure to exit?",parent=self.root)
		if self.iExit > 0:
			self.root.destroy()
		else:
			return			

	#Function Buttons	

	def student_details(self):
		self.new_window=Toplevel(self.root)
		self.app=Student(self.new_window)

	#Train func
	def train_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Train(self.new_window)


	#Face Detector Func
	def face_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Face_Recognition(self.new_window)
	

		
	#Attendance Func
	def attendance_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Attendance(self.new_window)	


	#Developer Func
	def developer_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Developer(self.new_window)		



	#HelpDesk Func
	'''def help_data(self):
		self.new_window=Toplevel(self.root)
		self.app=Help(self.new_window)'''

	#Chat bot
	def chatbot(self):
		self.new_window=Toplevel(self.root)
		self.app=ChatBot(self.new_window)			





if __name__=="__main__":
	root=Tk()
	obj=Face_Recognition_System(root)
	root.mainloop()








