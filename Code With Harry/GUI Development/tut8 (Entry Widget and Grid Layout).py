'''
Author: Jay Patil
Date: 24 August 2020
Purpose: Learning Python
'''

from tkinter import *
root = Tk()
root.geometry("655x333")

def getvals():
    print(f"The user name is {user_value.get()}")
    print(f"The password is {pass_vaue.get()}")

user = Label(root,text="Username")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

# Variable Classes in Tkinter
# 1 BooleanVar
# 2 DoubleVar
# 3 IntVar
# 4 StringVar

user_value = StringVar()
pass_vaue = StringVar()

user_Entry = Entry(root, textvariable=user_value)
pass_Entry = Entry(root, textvariable=pass_vaue)
user_Entry.grid(row=0,column=1)
pass_Entry.grid(row=1,column=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()
