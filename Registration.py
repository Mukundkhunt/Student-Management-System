from tkinter import *
import pymysql
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
class Registration:
   def __init__(self,root):
      self.root = root
      self.root.title("Registration Form")
      self.big_icon = ImageTk.PhotoImage(file = "images/2.jpg")
      self.root.geometry("1920x1080+0+0")
      bg_lbl = Label(self.root, image = self.big_icon, height=1080, width = 1920).pack()
      title = Label(self.root, text = "Registration Form", bd = 10, relief = GROOVE, font = ("times new roman", 40, "bold"), bg = "#FECEA8", fg = "#2A363B")
      title.place(x=0, y=0, relwidth = 1)
      self.Enrolment_no=StringVar()
      self.Fullname=StringVar()
      self.Email=StringVar()
      self.Gender = StringVar()
      self.Contact_var = StringVar()
      self.DOB_var = StringVar()
      self.address_var = StringVar()
   #c=StringVar()
   #var1= IntVar()

      Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE ,bg = "#271E1C")
      Manage_Frame.place(x = 647, y = 150, width = 620, height = 550)
             
#label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
#label_0.place(x=90,y=53)

      label_4 = Label(self.root, text="Enrolment No",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_4.place(x=650,y=180)

      entry_4 = Entry(self.root,textvar=self.Enrolment_no,font = ("times new roman", 15, "bold"))
      entry_4.place(x=950,y=180)

      label_1 = Label(self.root, text="Full Name",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_1.place(x=650,y=240)

      entry_1 = Entry(self.root,textvar=self.Fullname,font = ("times new roman", 15, "bold"))
      entry_1.place(x=950,y=240)

      label_2 = Label(self.root, text="Email",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_2.place(x=650,y=300)

      entry_2 = Entry(self.root,textvar=self.Email,font = ("times new roman", 15, "bold"))
      entry_2.place(x=950,y=300)

      label_3 = Label(self.root, text="Gender",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_3.place(x=650,y=360)

#Radiobutton(root, text="Male",padx = 5, variable=Gender, value=1,font = ("times new roman", 12, "bold"),fg = "#FFFFFF",bg = "#271E1C").place(x=950,y=360)
#Radiobutton(root, text="Female",padx = 20, variable=Gender, value=2,font = ("times new roman", 12, "bold"),fg = "#FFFFFF",bg = "#271E1C").place(x=1040,y=360)
      combo_gender = ttk.Combobox(self.root, textvariable = self.Gender, font = ("times new roman", 12), state = "readonly")
      combo_gender['values'] = ("Male", "Female", "Other")
      combo_gender.place(x=950,y=360)


      label_4 = Label(self.root, text="Contact No",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_4.place(x=650,y=420)

      entry_4 = Entry(self.root,textvar=self.Contact_var,font = ("times new roman", 15, "bold"))
      entry_4.place(x=950,y=420)

      label_6 = Label(self.root, text="D.O.B.",width=20,font = ("times new roman", 15, "bold"),fg = "#38E4DF",bg = "#271E1C")
      label_6.place(x=650,y=480)

      entry_6 = Entry(self.root,textvar=self.DOB_var,font = ("times new roman", 15, "bold"))
      entry_6.place(x=950,y=480)

      lbl_Address = Label(self.root, text = "Address",width=20,fg = "#38E4DF",bg = "#271E1C", font = ("times new roman", 15, "bold"))
      lbl_Address.place(x=650,y=540)


      txt_Address = Entry(self.root,textvar=self.address_var,font = ("times new roman", 15, "bold"))
      txt_Address.place(x=950,y=540)
   
      Button(root, text='Submit',width=20,bg='brown',fg='white',command=self.database1).place(x=850,y=615)


   def database1(self):
      conn = pymysql.connect(host = 'database.c4mqwpgn7flf.ap-south-1.rds.amazonaws.com', user = 'admin', password = 'admin123', database = "db")
      cursor=conn.cursor()
      cursor.execute('INSERT INTO students values(%s,%s,%s,%s,%s,%s,%s)',(self.Enrolment_no.get(),self.Fullname.get(),self.Email.get(),self.Gender.get(),self.Contact_var.get(),self.DOB_var.get(),self.address_var.get()))
      conn.commit()
      messagebox.showinfo("Success", "Registration has been completed.")
      conn.close()
   
 
"""label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="java", variable=var1).place(x=235,y=330)

Checkbutton(root, text="python", variable=var2).place(x=290,y=330)
"""
root = Tk()
obj = Registration(root)
root.mainloop()