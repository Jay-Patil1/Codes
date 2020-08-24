'''
Author: Jay Patil
Date: 24 August 2020
Purpose: Learning Python
'''

from tkinter import *
root = Tk()
root.geometry("655x333")

def Hello():
    print("Hello This a TKINTER button.")

def Name():
    print("Name is JAY.")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=TOP,anchor="nw")

b1 = Button(frame,fg="red", text="Print Now",command=Hello)
b1.pack(side=LEFT, padx=20,pady=20)

b2 = Button(frame,fg="red", text="Print Name",command=Name)
b2.pack(side=LEFT, padx=20,pady=20)

b3 = Button(frame,fg="red", text="Print Now 1")
b3.pack(side=LEFT, padx=20,pady=20)

b4 = Button(frame,fg="red", text="Print Now 2")
b4.pack(side=LEFT, padx=20,pady=20)

root.mainloop()
