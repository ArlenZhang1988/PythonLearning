from tkinter import *

def ChangeText():
    var.set("Yes she is.")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("She is the cutest person \n in the world")

textLabel = Label(frame1,textvariable  = var,
                justify = LEFT,
                padx = 10)
textLabel.pack(side = LEFT)

# error when using image
#photo = PhotoImage(file = "aragaki_lesson66.jpg")
#imageLabel = Label(root,image = photo)
#imageLabel.pack()

button = Button(frame2,text = "No she is not.",command = ChangeText)
button.pack()

frame1.pack(padx = 10,pady = 10)
frame2.pack(padx = 10, pady = 10)

mainloop()