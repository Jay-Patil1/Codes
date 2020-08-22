from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import os

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Studemt Management System")
        self.root.geometry("1584x832+0+0")

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40, "bold"),bg="yellow",fg="red")
        title.pack(side=TOP, fill=X)

    # All Variables #

        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()
        
        
    # Manage Frame #

        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=105,width=510,height=705)

        m_title = Label(Manage_Frame,text="Manage Students",bg="crimson",fg="black",relief=GROOVE,bd=2,font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=40,padx=90)

        lbl_roll = Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=35,sticky="w")

        self.txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=35,sticky="w")

        self.txt_name = Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email = Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=35,sticky="w")

        self.txt_email = Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender = Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=35,sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male", "Female", "Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=25,sticky="w")

        lbl_contact = Label(Manage_Frame,text="Conatct",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=35,sticky="w")

        self.txt_contact = Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DoB = Label(Manage_Frame,text="D.O.B.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DoB.grid(row=6,column=0,pady=10,padx=35,sticky="w")

        self.txt_DoB = Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_DoB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address = Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=35,sticky="w")

        self.txt_Address = Text(Manage_Frame,width=30,height=5,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        self.txt_Roll.focus()

    # Button Frame #
        
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=8,y=580,width=487)

        Addbtn = Button(btn_Frame,text="Add", width=10,command=self.add_Student,font=("timew new roman", 13))
        Addbtn.bind("<Return>",self.add_Student)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)
        
        Updatebtn = Button(btn_Frame,text="Update", width=10,command=self.update_data,font=("timew new roman", 13))
        Updatebtn.bind("<Return>",self.update_data)
        Updatebtn.grid(row=0,column=1,padx=10,pady=10)
        
        Deletebtn = Button(btn_Frame,text="Delete", width=10,command=self.delete_Data,font=("timew new roman", 13))
        Deletebtn.bind("<Return>",self.delete_Data)
        Deletebtn.grid(row=0,column=2,padx=10,pady=10)
        
        Clearbtn = Button(btn_Frame,text="Clear", width=10,command=self.clear,font=("timew new roman", 13))
        Clearbtn.bind("<Return>",self.clear)
        Clearbtn.grid(row=0,column=3,padx=10,pady=10)
        
        LogOutbtn = Button(Manage_Frame,text="Log-Out", width=10,command=self.LogOut,font=("timew new roman", 13))
        LogOutbtn.bind("<Return>",self.LogOut)
        LogOutbtn.place(x=390,y=653)

    # Detail Frame #

        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=557,y=105,width=1000,height=705)

        lbl_Search = Label(Detail_Frame,text="Search By:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=50,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.Search_by,width=10,font=("times new roman",14,"bold"),state="readonly")
        combo_search['values']=("Roll_No", "Name", "Contact")
        combo_search.grid(row=0,column=1,pady=15,padx=20,sticky="w")

        txt_search = Entry(Detail_Frame,textvariable=self.Search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_search.bind("<Return>",self.search_Data)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        Searchbtn = Button(Detail_Frame,text="Search",width=10,command=self.search_Data,font=("timew new roman", 13))
        Searchbtn.bind("<Return>",self.search_Data)
        Searchbtn.grid(row=0,column=3,padx=20,pady=15)
        
        Showallbtn = Button(Detail_Frame,text="Show All",width=10,command=self.fetch_Data,font=("timew new roman", 13))
        Showallbtn.bind("<Return>",self.fetch_Data)
        Showallbtn.grid(row=0,column=4,padx=20,pady=15,sticky="e")
        
    # Table Frame #

        Tabel_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Tabel_Frame.place(x=25,y=70,width=940,height=600)

        scroll_x = Scrollbar(Tabel_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Tabel_Frame,orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Tabel_Frame,columns=("Roll","Name","Email","Gender","Contact","D.O.B.","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Roll", text="Roll No.")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Email", text="Email")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("D.O.B.", text="D.O.B.")
        self.Student_Table.heading("Address", text="Address")
        self.Student_Table['show']='headings'
        self.Student_Table.column('Roll',width=40)
        self.Student_Table.column('Name',width=100)
        self.Student_Table.column('Email',width=150)
        self.Student_Table.column('Gender',width=20)
        self.Student_Table.column('Contact',width=60)
        self.Student_Table.column('D.O.B.',width=50)
        self.Student_Table.column('Address',width=180)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.Student_Table.pack(fill=BOTH,expand=1)
        self.fetch_Data()

    def add_Student(self,*args):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All the fields are required.")

        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="StM")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
            self.Roll_No_var.get(),
            self.Name_var.get() ,
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.DOB_var.get(),
            self.txt_Address.get('1.0',END)
            ))
            con.commit()
            self.fetch_Data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Data Added.")

    def fetch_Data(self,*args):
        con = pymysql.connect(host="localhost",user="root",password="",database="StM")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
                con.commit()
        self.Search_by.set("")
        self.Search_txt.set("")
        con.close()

    def clear(self,*args):
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.txt_Address.delete('1.0',END)

    def get_cursor(self,ev,*args):   # We have to give any 2 arguements so ev is given.
        cursor_row = self.Student_Table.focus()       
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        # print(row)
        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6])
    
    def update_data(self,*args):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All the fields are required.\nYou can select the student by clicking.")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="StM")
            cur = con.cursor()
            cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
            self.Name_var.get() ,
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.DOB_var.get(),
            self.txt_Address.get('1.0',END),
            self.Roll_No_var.get()
            ))
            con.commit()
            self.fetch_Data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Data Updated.")

    def delete_Data(self,*args):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Email_var.get()=="" or self.Gender_var.get()=="" or self.Contact_var.get()=="" or self.DOB_var.get()=="" or self.txt_Address.get('1.0',END)=="":
            messagebox.showerror("Error","All the fields are required.\nYou can select the student by clicking.")
        else:
            self.askdel = messagebox.askyesno("Delete", "Do you want to delete the selected Student?")
            if self.askdel>0:
                con = pymysql.connect(host="localhost",user="root",password="",database="StM")
                cur = con.cursor()
                cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
                con.commit()
                con.close()
                self.fetch_Data()
                self.clear()
                messagebox.showinfo("Success","Data Deleted.") 
            else:
                self.clear

    def search_Data(self,*args):
        con = pymysql.connect(host="localhost",user="root",password="",database="StM")
        cur = con.cursor()

        cur.execute("select * from students where "+str(self.Search_by.get())+" LIKE '%"+str(self.Search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
                con.commit()
        con.close()

    def LogOut(self,*args):
        of = "C:\\Users\\SHREE\\Jay (Coding)\\Web Code\\Login System.py"
        os.startfile(of)
        exit()

root = Tk()
ob = Student(root)
root.mainloop()
