import csv
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

from PIL import Image, ImageTk

mydata=[]  #declaring global variable for importing csv file
class Attendance:
	def __init__(self, root):
		self.root=root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")

		#Text variables

		self.var_atten_id=StringVar()
		self.var_atten_reg=StringVar()
		self.var_atten_name=StringVar()
		self.var_atten_dep=StringVar()
		self.var_atten_time=StringVar()
		self.var_atten_date=StringVar()
		self.var_atten_attendance=StringVar()

    #second image section======

		#background image=======
		img3=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\background.jpg")
		
		img3=img3.resize((2000,710),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=0,width=2000,height=1000)

		#Title bar above background image======	
		title_lbl=Label(bg_img,text="STUDENT ATTENDANCE",font=("Sketchy In Snow", 25,"bold"),bg="purple",fg="white")
		title_lbl.place(x=-120,y=0,width=1530,height=45)

		main_frame=Frame(bg_img,bd=2, bg="violet")
		main_frame.place(x=0,y=50,width=1300,height=750)

		#left frame label
		Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=FLAT,text="Student Attendance Details",font=("times new roman",12,"bold"))
		Left_frame.place(x=10,y=10,width=800,height=580)

		img_left=Image.open(r"C:\Users\DELL\Desktop\Face-Recognition-System-main\img\group cls 02.jpg")
		
		img_left=img_left.resize((720,130),Image.ANTIALIAS)
		self.photoimg_left=ImageTk.PhotoImage(img_left)

		f_lbl=Label(Left_frame,image=self.photoimg_left)
		f_lbl.place(x=5,y=0,width=0,height=0)

		left_inside_frame=Frame(Left_frame,bd=2,relief=SOLID, bg="white")
		left_inside_frame.place(x=0,y=10,width=1000,height=550)

		#label and entry
		attendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
		attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

		attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
		attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

		#Reg
		regLabel=Label(left_inside_frame,text="Reg:",font=("times new roman",11,"bold"),bg="white")
		regLabel.grid(row=0,column=2,padx=4,pady=8,sticky=W)

		atten_reg=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_reg,font=("times new roman",12,"bold"))
		atten_reg.grid(row=0,column=3,pady=8,sticky=W)

		#Name
		nameLabel=Label(left_inside_frame,text="Name:",font=("times new roman",11,"bold"),bg="white")
		nameLabel.grid(row=1,column=0,padx=4,sticky=W)

		atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
		atten_name.grid(row=1,column=1,pady=8,padx=10,sticky=W)

		#Department
		depLabel=Label(left_inside_frame,text="Department:",font=("times new roman",11,"bold"),bg="white")
		depLabel.grid(row=1,column=2,padx=4,sticky=W)

		atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
		atten_dep.grid(row=1,column=3,pady=8,sticky=W)


		#Time
		timeLabel=Label(left_inside_frame,text="Time:",font=("times new roman",11,"bold"),bg="white")
		timeLabel.grid(row=2,column=0,padx=4,sticky=W)

		atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
		atten_time.grid(row=2,column=1,pady=8,padx=10,sticky=W)


		#Date
		dateLabel=Label(left_inside_frame,text="Date:",font=("times new roman",11,"bold"),bg="white")
		dateLabel.grid(row=2,column=2,padx=4,sticky=W)

		atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
		atten_date.grid(row=2,column=3,pady=8,sticky=W)

		#Attendance
		attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",11,"bold"),bg="white")
		attendanceLabel.grid(row=3,column=0,padx=2,sticky=W)

		self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsans 11 bold", state="readonly")
		self.atten_status["values"]=("Status","Present","Absent")
		self.atten_status.grid(row=3,column=1,pady=2)
		self.atten_status.current(0)


		#buttons frame
		btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
		btn_frame.place(x=0,y=500,width=800,height=35)

		save_btn=Button(btn_frame,text="Import csv",width=16,command=self.importCsv,font=("times new roman",11,"bold"),bg="purple",fg="white")
		save_btn.grid(row=0,column=0)

		update_btn=Button(btn_frame,text="Export csv",width=17,command=self.exportCsv,font=("times new roman",11,"bold"),bg="purple",fg="white")
		update_btn.grid(row=0,column=1)

		delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",11,"bold"),bg="purple",fg="white")
		delete_btn.grid(row=0,column=2)

		reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",11,"bold"),bg="purple",fg="white")
		reset_btn.grid(row=0,column=3)


		#right frame label
		Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",11,"bold"))
		Right_frame.place(x=650,y=10,width=720,height=580)


		table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
		table_frame.place(x=5,y=5,width=600,height=555)

		#=====Scroll Bar====
		scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

		self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","reg","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)


		scroll_x.config(command=self.AttendanceReportTable.xview)
		scroll_y.config(command=self.AttendanceReportTable.yview)

		self.AttendanceReportTable.heading("id",text="Attendance ID")
		self.AttendanceReportTable.heading("reg",text="Registration No")
		self.AttendanceReportTable.heading("name",text="Name")

		self.AttendanceReportTable.heading("department",text="Department")
		self.AttendanceReportTable.heading("time",text="Time")
		self.AttendanceReportTable.heading("date",text="Date")
		self.AttendanceReportTable.heading("attendance",text="Attendance")


		self.AttendanceReportTable["show"]="headings"

		#Setting column width
		self.AttendanceReportTable.column("id",width=100)
		self.AttendanceReportTable.column("reg",width=100)
		self.AttendanceReportTable.column("name",width=100)

		self.AttendanceReportTable.column("department",width=100)
		self.AttendanceReportTable.column("time",width=100)
		self.AttendanceReportTable.column("date",width=100)
		self.AttendanceReportTable.column("attendance",width=100)

		self.AttendanceReportTable.pack(fill=BOTH, expand=1)

		self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



	#========Fetch Data=========
	def fetchData(self,rows):
		self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
		for i in rows:
			self.AttendanceReportTable.insert("",END,values=i)

	
	#Importing csv func
	def importCsv(self):
		global mydata
		mydata.clear()
		fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
		with open(fln) as myfile:
			csvread=csv.reader(myfile,delimiter=",")
			for i in csvread:
				mydata.append(i)
			self.fetchData(mydata)				

	

	#Exporting CSV
	def exportCsv(self):
		try:
			if len(mydata)<1:
				messagebox.showerror("No Data", "No Data found to export",parent=self.root)
				return False
			fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)	

			with open(fln,mode="w",newline="") as myfile:
				exp_write=csv.writer(myfile,delimiter=",")
				for i in mydata:
					exp_write.writerow(i)
				messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+  "successfully")
				
		except Exception as es:
			messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)				

	

	#Showing data for text variables entry fields
	def get_cursor(self, event=""):
		cursor_row=self.AttendanceReportTable.focus()
		content=self.AttendanceReportTable.item(cursor_row)
		rows=content['values']
		self.var_atten_id.set(rows[0])
		self.var_atten_reg.set(rows[1])
		self.var_atten_name.set(rows[2])
		self.var_atten_dep.set(rows[3])
		self.var_atten_time.set(rows[4])
		self.var_atten_date.set(rows[5])
		self.var_atten_attendance.set(rows[6])

	#Reset Func
	def reset_data(self):
		self.var_atten_id.set("")
		self.var_atten_reg.set("")
		self.var_atten_name.set("")
		self.var_atten_dep.set("")
		self.var_atten_time.set("")
		self.var_atten_date.set("")
		self.var_atten_attendance.set("")



																																																			
if __name__=="__main__":
	root=Tk()
	obj=Attendance(root)
	root.mainloop()	