from tkinter import *

# learning canvas
root  = Tk()

w = Canvas(root,width = 200,height = 100,background = "Blue")
w.pack()

l1 = w.create_line(0,50,200,50,fill = "yellow") # create_line. p1 = start from x axis, p2 = y axisfill = start from line color, p3 and p4 are the end of axis
l2 = w.create_line(100,0,100,100,fill = "red",dash = (4,4)) # dash = dot line
r1 = w.create_rectangle(50,25,150,75,fill=  "blue")

w.coords(l1,0,25,200,25)
w.itemconfig(r1,fill = "red")
w.delete(l2)

w.create_text(100,50,text="Love")

Button(root,text = "Delete all",command = (lambda x = ALL: w.delete(x))).pack()

mainloop()