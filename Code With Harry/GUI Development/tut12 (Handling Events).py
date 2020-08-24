'''
Author: Jay Patil
Date: 24 August 2020
Purpose: Learning Python
'''

from tkinter import *
root = Tk()
root.title("Events in Tkinter")
root.geometry("644x534")

def jay(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

widget = Button(root,text="Click Me")
widget.pack()
widget.bind('<Button-1>',jay)  # Events can be googled.
widget.bind('<Double-1>',quit)

root.mainloop()
