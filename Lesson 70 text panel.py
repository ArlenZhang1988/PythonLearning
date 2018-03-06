# learning text
from tkinter import *

root = Tk()

text = Text(root,width = 300,height = 200)
text.pack()

text.insert(INSERT,"I love \n")
text.insert(END,"it \n")

# add a button and an image to the text
#photo = PhotoImage(file = "aragaki_lesson66.jpg")
b1 = Button(text, text = "click me",command = lambda : text.image_create(END,image =NONE))
text.window_create(END,window = b1)

mainloop()