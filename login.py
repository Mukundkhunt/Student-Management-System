from tkinter import messagebox
import tkinter as tk
from tkinter import*
from PIL import ImageTk
import Student
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1920x1080+0+0")
        #============All Images===============
        self.big_icon = ImageTk.PhotoImage(file = "images/bg.png")
        self.user_icon = PhotoImage(file = "images/user_name.png")
        self.pass_icon = PhotoImage(file = "images/password.png")
        self.logo_icon = PhotoImage(file = "images/logo.png")

        #========= Vaiables ==============
        self.uname = StringVar()
        self.pass_ = StringVar()



        bg_lbl = Label(self.root, image = self.big_icon).pack()

        title = Label(self.root,text = "Login System",font = ("times new roman", 40, "bold"),bg = "#6E9BA5", fg = "black", bd = 10, relief = GROOVE)
        title.place(x=0, y=0, relwidth = 1)

        Login_Frame = Frame(self.root, bg = "white")
        Login_Frame.place(x = 830, y = 280)
        logolbl = Label(Login_Frame, image = self.logo_icon, bd = 0).grid(row = 0, columnspan = 2)
       
        lbluser = Label(Login_Frame, text = "Username", image = self.user_icon, compound = LEFT, font = ("times new roman", 10, "bold"), bg = "white").grid(row = 1,column = 0, padx = 10, pady = 10)
        txtuser = Entry(Login_Frame, bd = 5, textvariable = self.uname, relief = GROOVE, font = ("", 10)).grid(row = 1, column = 1, padx = 10)

        lblpass = Label(Login_Frame, text = "Password", image = self.pass_icon, compound = LEFT, font = ("times new roman", 10, "bold"), bg = "white").grid(row = 2,column = 0, padx = 10, pady = 10)
        txtpass = Entry(Login_Frame, bd = 5, textvariable = self.pass_, relief = GROOVE, font = ("", 10)).grid(row = 2, column = 1, padx = 10)

        btn_log = Button(Login_Frame, text = "Login", width = 15,command = self.login, font = ("times new roman", 14 ,"bold"), bg = "cyan" ,fg = "black").grid(row = 3, column = 1, pady = 10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "" :
            messagebox.showerror("Error", "All fields are required !!")
        elif self.uname.get() == "Mukund" and self.pass_.get() == "mk123" :
            messagebox.showerror("Successfull", f"Welcome {self.uname.get()}")
            #root1 = Tk()
            obj2 = Student.Student(root).tkraise()
            #root1.mainloop()
        else :
            messagebox.showerror("Error", "!! Invalid username or password !!")

root = Tk()
obj = Login_System(root)
root.mainloop()