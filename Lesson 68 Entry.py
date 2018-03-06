from tkinter import *

# Entry
root = Tk()

e = Entry(root)
e.pack(padx = 20,pady = 20)

e.delete(0,END)
e.insert(0,"Default text")

mainloop()

# Entry practice (Using grid)


