'''
Author: Jay Patil
Date: 24 August 2020
Purpose: Learning Python
'''

from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Jay's GUI")
can_widget = Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# Line goes from the point x1, y1 to x2, y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="blue")

# To create rectangle give coordinates of:-
# Top Left
# Bottom Right
can_widget.create_rectangle(65,100,700,300,fill="blue")

# To create oval give coordinates of rectangle in which the oval is suppposed to be.
can_widget.create_oval(65,100,700,300,fill="yellow")

# To create text give coordinates of the center.
can_widget.create_text(400,200,text="Python",fill="red",font="timesnewroman 23 bold")

# To create circle give to right and bottom left coordinates of square.

root.mainloop()
