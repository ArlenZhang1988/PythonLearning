from tkinter import *

root = Tk()

def PrintValue():
    print(textArray[0] + " : "+ e1.get())
    print(textArray[1] + " : "+ e2.get())
    e1.delete(0,END)
    e2.delete(0,END)

textArray = ("Who is your favorite person?","How old is she?")
v1 = StringVar()
v2 = StringVar()

Label(root,text = textArray[0]).grid(row = 0,column = 0)

e1 = Entry(root,textvariable = v1)
e1.grid(row = 0,column = 1,padx = 10,pady = 5)

Label(root,text = textArray[1]).grid(row = 1,column = 0)

e2 = Entry(root,textvariable = v2,show = "*") # use show parameter to make a password entry.
e2.grid(row = 1,column = 1,padx = 10,pady = 5)

b = Button(root,text = "Submit", width = 10,command = PrintValue).grid(row = 3,column = 0,sticky = W)

b2 = Button(root,text = "Exit", command =root.quit()).grid(row = 3,column = 1,sticky = E)

mainloop()