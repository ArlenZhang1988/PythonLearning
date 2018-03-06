from tkinter import*

# create a menu

root = Tk()

menuBar = Menu(root)

# drop down menu
fileMenu = Menu(menuBar,tearoff = False) # tearoff = True mean the menu can be separate into different panel
fileMenu.add_command(label = "Open",command = (lambda : print("Hi")))
fileMenu.add_command(label = "Save")
fileMenu.add_separator()
fileMenu.add_command(label = "Quit",command = root.quit())
menuBar.add_cascade(label = "File",menu = fileMenu)

editMenu = Menu(menuBar,tearoff = False)
editMenu.add_command(label = "Cut",command = (lambda : print("Hi")))
editMenu.add_command(label = "Copy",command = (lambda : print("Hi")))
editMenu.add_command(label = "Paste",command = (lambda : print("Hi")))
menuBar.add_cascade(label = "Edit",menu = editMenu)

# pop menu(right click)
popMenu = Menu(root)
popMenu.add_command(label = "Remake")

frame = Frame(root,width = 512,height = 512)
frame.pack()

def PopMenu(event):
    popMenu.post(event.x_root,event.y_root)

frame.bind("<Button-3>",PopMenu)

# you can create menubutton
# Menubutton(root,text = string,relief = RAISED).pack()

# option menu
# OptionMenu(root,StringVar() instance,"values1","values2","valuesn").pack()

root.config(menu = menuBar)

mainloop()