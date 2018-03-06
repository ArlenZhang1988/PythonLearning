from tkinter import *

root = Tk()

# learning grid
Label(root,text ="Account: ").grid(row = 0,sticky = W)
Label(root,text ="Password: ").grid(row = 1, sticky = W)

Entry(root).grid(row = 0, column = 1)
Entry(root,show = "*").grid(row = 1, column = 1)

mainloop()