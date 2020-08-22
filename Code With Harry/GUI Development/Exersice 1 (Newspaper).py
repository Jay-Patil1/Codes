# NEWSPAPER
'''
Author: Jay Patil
Date: 22 August 2020
Purpose: Learning Python
'''

                # SOLUTION

from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Aapka Apna Akhabaar")
root.geometry("785x838")

def every_100(text):
    final_text = ""
    for i in range (0, len(text)):
        final_text += text[i]
        if i%100==0 and i != 0:
            final_text += "\n"
    return final_text

texts = []
photos = []
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.png")
    #TODO: Resize Images
    image = image.resize((255,230),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=1000,height=70)
Label(f0,text="Jay Patil News", font="Lucida 33 bold").pack()
f0.pack()
Label(f0,text="August 22 2020", font="Lucida 15 bold").pack()
f0.pack()

f1 = Frame(root, width=900,height=50,pady=10,padx=80)
Label(f1, text=texts[0],padx=22, pady=22).pack(side="left")
Label(f1, image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2 = Frame(root, width=900,height=50,pady=10,padx=80)
Label(f2, text=texts[1],padx=22, pady=22).pack(side="right")
Label(f2, image=photos[1],anchor="e").pack()
f2.pack(anchor="w")

f3 = Frame(root, width=900,height=50,pady=10,padx=80)
Label(f3, text=texts[2],padx=22, pady=22).pack(side="left")
Label(f3, image=photos[2],anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()
