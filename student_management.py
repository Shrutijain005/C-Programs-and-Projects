from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector



class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Student Mangement System")

        title = Label(self.root, text="Student Mangement System", bd=4, relief=RAISED, font=("Calibri", 30, "bold"), bg='powder blue', fg='black')
        title.pack(side=TOP, fill='x')

        ###########ALL VARIABLE##########
        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.txt_address = StringVar()
        
        ###########MANAGE FRAME##########
        Manage = Frame(self.root, bd=4, relief=RIDGE, bg='powder blue')
        Manage.place(x=20, y=80, width=550, height=660)

        m_title = Label(Manage, text="Manage Student", bg='powder blue', fg='black', font=('calibri', 30, 'bold'), bd=4, relief=RAISED, width=20)
        m_title.grid(row=0, columnspan=2, pady=20, padx=55)

        lbl_roll = Label(Manage, text="Roll Number", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        txt_roll = Entry(Manage, textvariable=self.roll_var, font=('calibri', 15, 'bold'), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')

        lbl_name = Label(Manage, text="Name", bg='powderblue', fg='black', font=('calibri', 20, 'bold'))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        txt_name = Entry(Manage, textvariable=self.name_var, font=( 'calibri', 15, 'bold'), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

        lbl_email = Label(Manage, text="Email", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        txt_email = Entry(Manage, textvariable=self.email_var, font=('calibri', 15, 'bold'), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')

        lbl_gender = Label(Manage, text="Gender", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')

        combo_gender = ttk.Combobox(Manage, textvariable=self.gender_var, width=19, font=('calibri', 15, 'bold'), state='readonly')
        combo_gender['values'] = ("Male", "Female", "Others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_contact = Label(Manage, text="Contact", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        txt_contact = Entry(Manage, textvariable=self.contact_var, font=('calibri', 15, 'bold'), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')

        lbl_dob = Label(Manage, text="D.O.B", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        txt_dob = Entry(Manage, textvariable=self.dob_var, font=('calibri', 15, 'bold'), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        lbl_address = Label(Manage, text="Address", bg='powderblue',fg='black', font=('calibri', 20, 'bold'))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        self.txt_address = Text(Manage, width=20, height=3, font=('calibri', 15, 'bold'), bd=5, relief=GROOVE)
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        ########BUTTON FRAME############
        btn_frame = Frame(self.root, bd=4, relief=RIDGE, bg='powder blue')
        btn_frame.place(x=30, y=650, width=528)

        Addbtn = Button(btn_frame, text="Add", width=13, height=2, fg='white', bg='crimson',command=self.add_student).grid(row=0, column=0, padx=15, pady=16)
        updatebtn = Button(btn_frame, text="Update", width=13, height=2,fg='white', bg='crimson', command=self.update_data).grid(row=0, column=1, padx=15, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=13, height=2, fg='white',bg='crimson', command=self.delete_data).grid(row=0, column=2, padx=15, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=13, height=2,fg='white', bg='crimson', command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        ###########DETAILS FRAME###########
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='powder blue')
        detail_frame.place(x=600, y=80, width=900, height=660)

        lbl_search = Label(detail_frame, text="Search",bg='powder blue', fg='black', font=('calibri', 20, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        
        self.search_by=StringVar()
        combo_search = ttk.Combobox(detail_frame, textvariable=self.search_by, font=('calibri', 13, 'bold'), width=10, state='readonly')
        combo_search['values'] = ("Name", "roll", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')
        self.search_txt=StringVar()
        txt_search = Entry(detail_frame, textvariable=self.search_txt, font=('calibri', 10, 'bold'), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')
        searchbtn = Button(detail_frame, text="Search", width=10, pady=5, command=self.search_data).grid( row=0, column=3, padx=12, pady=10)
        showallbtn = Button(detail_frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=14, pady=14)

        ###########TABLE FRAME###########
        Table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg='crimson')
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_frame, columns=("roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Roll Number")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_student(self):

        if self.roll_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "please fill all the fields!!!")

        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Sj2000005!", database="mydata")
            cur = con.cursor()

            cur.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s)", (self.roll_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.txt_address.get('1.0', END)))

            con.commit()
            # this is for if we add any new student then it will call and update the pool
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Successfull", "Record has been inserted.")

    def fetch_data(self):

        con = mysql.connector.connect(host="localhost", user="root", password="Sj2000005!", database="mydata")
        cur = con.cursor()

        cur.execute("select * from student")
        rows = cur.fetchall()
        if(len(rows) != 0):
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

            con.commit()
        con.close()

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete('1.0', END)

    def get_cursor(self, event=""):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[6])

    def update_data(self):
        if self.roll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")
        else:
            con = mysql.connector.connect(
            host="localhost", user="root", password="Sj2000005!", database="mydata")
            cur = con.cursor()

            cur.execute("update student set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll=%s", (self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.contact_var.get(), self.dob_var.get(), self.txt_address.get('1.0', END), self.roll_var.get()))

            con.commit()
        # this is for if we add any new student then it will call and update the pool
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Update", "Record has been updated.")

    def delete_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="Sj2000005!", database="mydata")
        cur = con.cursor()
        query="delete from student where roll=%s"
        value=(self.roll_var.get(),)
        cur.execute(query,value)
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Delete", "Record has been deleted.")

    def search_data(self):
        if self.search_by.get()=="" or self.search_txt.get()=="":
            messagebox.showerror("No", "Not availabe!")
        else:
            try:    
                con = mysql.connector.connect(host="localhost", username="root", password="Sj2000005!", database="mydata")
                cur = con.cursor()
                val=cur.execute("select * from student where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()
                if(len(rows)!= 0):
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                        self.Student_table.insert("",END,values=row)
                    con.commit()
                else:
                    messagebox.showinfo("No", "Not availabe!")    
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)   

class student():
    pass
    root = Tk()
    obj = student(root)
    root.mainloop()
