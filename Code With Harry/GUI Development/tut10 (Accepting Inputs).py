'''
Author: Jay Patil
Date: 24 August 2020
Purpose: Learning Python
'''

from tkinter import *
root = Tk()
root.geometry("350x250")
root.maxsize(350,250)
root.minsize(350,250)

def getvals():
    print("Sumbmitting Form")
    print(f"{nameval.get(),phoneval.get(),genderval.get(),emergencyval.get(),paymentval.get(),foodserviceval.get()}")
    with open("records.txt","a") as f:
        f.write(f"{nameval.get(),phoneval.get(),genderval.get(),emergencyval.get(),paymentval.get(),foodserviceval.get()}\n")

# Heading
Label(root,text="Welcome to Jay Travels",font="comiscansms 13 bold",pady=20).grid(row=0,column=3)

# Text Lables
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact",padx=10)
payment = Label(root, text="Payment Mode")

# Packing Text Lables
name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
payment.grid(row=5,column=1)

# Variables
nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emergencyval = StringVar()
paymentval = StringVar()
foodserviceval = IntVar()  # If Check Button checked then 1 and if unchecked then 0.

# Entries
nameentry = Entry(root,textvariable=nameval)
phoneentry = Entry(root,textvariable=phoneval)
genderentry = Entry(root,textvariable=genderval)
emergencyentry = Entry(root,textvariable=emergencyval)
paymententry = Entry(root,textvariable=paymentval)

# Packing Entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)

# Checkbox and Packing
foodservice = Checkbutton(text="Want to Prebook your meals?",variable=foodserviceval)
foodservice.grid(row=6,column=3)

# Button Packing it  and Assing command
Button(text="Submit to Jay Travels",command=getvals).grid(row=7,column=3)

root.mainloop()

