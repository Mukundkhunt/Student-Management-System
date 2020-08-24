from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import re
end_point = 'database.c4mqwpgn7flf.ap-south-1.rds.amazonaws.com'
usename = 'admin'
pass_word = 'admin123'
#con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
class Student :
    
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        
        self.big_icon = ImageTk.PhotoImage(file = "images/1.jpg")
        self.root.geometry("1920x1080+0+0")
        bg_lbl = Label(self.root, image = self.big_icon, height=1080, width = 1920).pack()
        

        title = Label(self.root, text = "Student Management System", bd = 10, relief = GROOVE, font = ("times new roman", 40, "bold"), bg = "#FECEA8", fg = "#2A363B")
        title.place(x=0, y=0, relwidth = 1)

    #========== All Variables ====================
        self.Enrolment_No_var = StringVar()
        self.Name_var = StringVar()
        self.Gender_var = StringVar()
        self.Email_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

    #================ Manage Frame =================

        Manage_Frame = Frame(self.root, bd = 4, relief = RIDGE ,bg = "#39CCCC")
        Manage_Frame.place(x = 170, y = 240, width = 476, height = 600)

        m_title = Label(Manage_Frame, text = "Manage Student", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 24, "bold"))
        m_title.grid(row = 0, columnspan = 2,padx = 70, pady = 6)

        #============ Enrolment No. ===================
        lbl_roll = Label(Manage_Frame, text = "Enrolment No.", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_roll.grid(row = 1, column = 0, padx = 20, pady = 6, sticky = "w")

        txt_roll = Entry(Manage_Frame, textvariable = self.Enrolment_No_var, font = ("times new roman", 12), bd = 5, relief = GROOVE)
        txt_roll.grid(row = 1, column = 1, padx = 10, pady = 6, sticky = "w")

        #============== Name =====================
        lbl_Name = Label(Manage_Frame, text = "Name", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Name.grid(row = 2, column = 0, padx = 20, pady = 6, sticky = "w")

        txt_Name = Entry(Manage_Frame, textvariable = self.Name_var, font = ("times new roman", 12), bd = 5, relief = GROOVE)
        txt_Name.grid(row = 2, column = 1, padx = 10, pady = 6, sticky = "w")

        #============ Email address ==============
        lbl_Email = Label(Manage_Frame, text = "Email", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Email.grid(row = 3, column = 0, padx = 20, pady = 6, sticky = "w")

        txt_Email = Entry(Manage_Frame, textvariable = self.Email_var, font = ("times new roman", 12), bd = 5, relief = GROOVE)
        txt_Email.grid(row = 3, column = 1, padx = 10, pady = 6, sticky = "w")

        #=========== Gender =============
        lbl_Gender = Label(Manage_Frame, text = "Gender", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Gender.grid(row = 4, column = 0, padx = 20, pady = 6, sticky = "w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable = self.Gender_var, font = ("times new roman", 12), state = "readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row = 4, column = 1, padx = 10, pady = 6, sticky = "w")

        #============ Contact Number ===========
        lbl_Contact = Label(Manage_Frame, text = "Contact No.", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Contact.grid(row = 5, column = 0, padx = 20, pady = 6, sticky = "w")

        txt_Contact = Entry(Manage_Frame, textvariable = self.Contact_var, font = ("times new roman", 12), bd = 5, relief = GROOVE)
        txt_Contact.grid(row = 5, column = 1, padx = 10, pady = 6, sticky = "w")

        #============ Date Of Birth(D.O.B.) =========
        lbl_DOB = Label(Manage_Frame, text = "Date Of Birth", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_DOB.grid(row = 6, column = 0, padx = 20, pady = 6, sticky = "w")

        txt_DOB = Entry(Manage_Frame, font = ("times new roman", 12), textvariable = self.DOB_var, bd = 5, relief = GROOVE)
        txt_DOB.grid(row = 6, column = 1, padx = 10, pady = 6, sticky = "w")

        #=========== Address =============
        lbl_Address = Label(Manage_Frame, text = "Address", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Address.grid(row = 7, column = 0, padx = 20, pady = 6, sticky = "w")

        self.txt_Address = Text(Manage_Frame, width = 17, height = 4, font = ("times new roman", 15))
        self.txt_Address.grid(row = 7, column = 1, padx = 10, pady = 6, sticky = "w")

        #==============Button Frame =================
        btn_Frame = Frame(Manage_Frame, bd = 4, relief = RIDGE, bg = "#39CCCC")
        btn_Frame.place(x = 10, y = 500, width = 446)

        Addbtn = Button(btn_Frame, text = "Add", width = 10, bg = "YELLOW", command = self.add_students).grid(row = 8, column = 0, padx = 10, pady = 6)
        Updatebtn = Button(btn_Frame, text = "Update", width = 10, bg = "YELLOW", command = self.update_data).grid(row = 8, column = 1, padx = 10, pady = 6)
        Deletebtn = Button(btn_Frame, text = "Delete", width = 10, bg = "YELLOW", command = self.delete_data).grid(row = 8, column = 2, padx = 10, pady = 6)
        Clearbtn = Button(btn_Frame, text = "Clear",command = self.clear, width = 10, bg = "YELLOW").grid(row = 8, column = 3, padx = 10, pady = 6)

    #============== Details Frame =================

        Detail_Frame = Frame(self.root, bd = 4, relief = RIDGE ,bg = "#39CCCC")
        Detail_Frame.place(x = 940, y = 240,width = 800, height = 600)

        lbl_Search = Label(Detail_Frame, text = "Search By", fg = "#001F3F", bg = "#39CCCC", font = ("times new roman", 15, "bold"))
        lbl_Search.grid(row = 0, column = 0, padx = 20, pady = 6, sticky = "w")

        combo_Search = ttk.Combobox(Detail_Frame, textvariable = self.search_by, font = ("times new roman", 10), state = "readonly")
        combo_Search['values'] = ("Enrolment_No", "Name", "Contact")
        combo_Search.grid(row = 0, column = 1, padx = 10, pady = 6, sticky = "w")

        txt_Search = Entry(Detail_Frame, textvariable = self.search_txt, font = ("times new roman", 12), bd = 5, relief = GROOVE)
        txt_Search.grid(row = 0, column = 2, padx = 10, pady = 6, sticky = "w")
        
        Search_btn = Button(Detail_Frame, text = "Search", width = 10, bg = "YELLOW", command = self.search_data).grid(row = 0, column = 3, padx = 10, pady = 6)
        Show_all_btn = Button(Detail_Frame, text = "Show All", width = 10, bg = "YELLOW", command = self.fetch_data).grid(row = 0, column = 4, padx = 10, pady = 6)

        #=============== Table Frame ==================
        Table_Frame = Frame(Detail_Frame, bd = 4, relief = RIDGE ,bg = "#39CCCC")
        Table_Frame.place(x = 10, y = 70,width = 760, height = 500)

        scroll_x = Scrollbar(Table_Frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient = VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns = ("Enrolment", "Name", "Email", "Gender", "Contact", "D.O.B.", "Address"), yscrollcommand = scroll_y.set, xscrollcommand = scroll_x.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.Student_table.xview)
        scroll_y.config(command = self.Student_table.yview)
        self.Student_table.heading("Enrolment", text = "Enrolment No")
        self.Student_table.heading("Name", text = "Name")
        self.Student_table.heading("Email", text = "Email")
        self.Student_table.heading("Gender", text = "Gender")
        self.Student_table.heading("Contact", text = "Contact")
        self.Student_table.heading("D.O.B.", text = "D.O.B.")
        self.Student_table.heading("Address", text = "Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Enrolment", width = 100)
        self.Student_table.column("Name", width = 150)
        self.Student_table.column("Email", width = 150)
        self.Student_table.column("Gender", width = 100)
        self.Student_table.column("Contact", width = 150)
        self.Student_table.column("D.O.B.", width = 100)
        self.Student_table.column("Address", width = 350)
        self.Student_table.pack(fill = BOTH, expand = 1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self) :
        if self.Enrolment_No_var.get() == "" or self.Name_var == "" :
            messagebox.showerror("Error", "All Fields adre required !!!")
        elif(len(self.Contact_var.get()) != 10) :
            messagebox.showerror("Error", "Contact Number should be 10")
        elif re.search("[0-9]", self.Name_var.get()) :
            messagebox.showerror("Error", "Name doesn't contain number")
        elif re.search("[A-Z]", self.Enrolment_No_var.get()) :
            messagebox.showerror("Error", "Enrolment No. doesn't contain alphabet")
        else :
            con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Enrolment_No_var.get(), self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(), self.Contact_var.get(), self.DOB_var.get(), self.txt_Address.get('1.0', END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been added.")

    def fetch_data(self):
        con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows :
                self.Student_table.insert('', END, values = row)
            con.commit()
        con.close()

    def clear(self) :
        self.Enrolment_No_var.set("")
        self.Name_var.set("")
        self.Gender_var.set("")
        self.Email_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev) :
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Enrolment_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Gender_var.set(row[2])
        self.Email_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self) :
        con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
        cur = con.cursor()
        cur.execute("update students set name = %s, email = %s, gender = %s, contact = %s, dob = %s, address = %s where enrolment_no = %s"
        , (self.Name_var.get(), self.Email_var.get(), self.Gender_var.get(), self.Contact_var.get(),
        self.DOB_var.get(), self.txt_Address.get('1.0', END), self.Enrolment_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
        cur = con.cursor()
        messagebox.showinfo("Success", f"Enrolment = {self.Enrolment_No_var.get()} && Name == {self.Name_var.get()} record has succesfully deleted")
        cur.execute("delete  from students where enrolment_no = %s", self.Enrolment_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        #con = pymysql.connect(host = "localhost", user = "", password = "", database = "db")
        #con = pymysql.connect(host = "localhost", user = "root", password = "", database = "Student_Management_System")
        con = pymysql.connect(host = end_point, user = usename, password = pass_word, database = "db")
        cur = con.cursor()
        cur.execute("select * from students where " + str(self.search_by.get()) + " Like '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows :
                self.Student_table.insert('', END, values = row)
            con.commit()
        con.close()



root = Tk()
obj = Student(root)
root.mainloop()