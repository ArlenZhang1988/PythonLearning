from tkinter import *

root = Tk()

# spin box
w = Spinbox(root,from_= 0, to_= 10)
w.pack()

s = Spinbox(root,values = ("Hi","おはよう","你好"))
s.pack()

# top level
def CreateTopLevel():
    top = Toplevel()
    top.attributes("-alpha",0.5) # change attributes
    top.title("Toplevel title") # change tittles

    msg = Message(top,text = "This is a message")
    msg.pack()

Button(root,text = "create top level", command = CreateTopLevel).pack()

mainloop()