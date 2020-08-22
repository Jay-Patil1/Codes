from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os



class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1584x832+0+0")

        # All Images #

        image = Image.open("bg.jpg")
        self.bg_icon = ImageTk.PhotoImage(image)
        self.user_icon = PhotoImage(file="images/user.png")
        self.pass_icon = PhotoImage(file="images/password.png")
        self.logo_icon = PhotoImage(file="images/logo.png")

        # Variables #
        
        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_Image = Label(self.root, image=self.bg_icon).pack(fill=Y)

        Title = Label(self.root, text="Login System", font=(
            "times new roman", 40, "bold"), bg="yellow", fg="red", bd=10, relief=GROOVE)
        Title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)

        logolbl = Label(Login_Frame, image=self.logo_icon,
                        bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT, font=(
            "times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname,
                        relief=GROOVE, font=("", 15))
        self.username = txtuser
        self.username.focus()
        txtuser.bind("<Return>",self.login)
        txtuser.grid(row=1, column=1, padx=20)

        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT, font=(
            "times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_,
                        relief=GROOVE, font=("", 15),show="*")
        txtpass.bind("<Return>",self.login)
        txtpass.grid(row=2, column=1, padx=20)
        self.password = txtpass


        btn_login = Button(Login_Frame, text="Login", width=15, command=self.login, font=(
            "times new roman", 14, "bold"), bg="yellow", fg="red")
        btn_login.bind("<Return>",self.login)
        btn_login.grid(row=3,column=0,pady=35,padx=10)

        btn_quit = Button(Login_Frame, text="Quit", width=15, command=self.quit, font=(
            "times new roman", 14, "bold"), bg="yellow", fg="red")
        btn_quit.bind("<Return>",self.quit)
        btn_quit.grid(row=3,column=1,pady=35,padx=10)

# Functions #

    def login(self,*args):
            of = "C:\\Users\\SHREE\\Jay (Coding)\\Web Code\\Student Management\\Student.py"
            
            if self.uname.get() == "" and self.pass_.get() == "":
                messagebox.showerror("Error", "All the fields are required!")
                self.username.focus()

            elif self.uname.get() == "":
                messagebox.showerror("Error", "UserName is required.")
                self.username.focus()

            elif self.uname.get() != "Jay Patil":
                messagebox.showerror("Error","Incorrect Username")
                self.username.focus()

            elif self.uname.get() == "Jay Patil":
                self.password.focus()
                if self.pass_.get() == "":
                    self.password.focus()
            
                elif self.pass_.get() != "Jay@123":
                    messagebox.showerror("Error","Incorrect Password")

                elif self.uname.get() == "Jay Patil" and self.pass_.get() == "Jay@123":
                    of = "C:\\Users\\SHREE\\Jay (Coding)\\Web Code\\Student Management\\Student.py"
                    messagebox.showinfo("Successfull Login",
                                        f"Welcome {self.uname.get()}\n\n Press OK to continue.")
                    os.startfile(of)
                    exit()

    def quit(self,*args):
        exit()

root = Tk()
obj = Login_System(root)
root.mainloop()

