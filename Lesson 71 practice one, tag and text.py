from tkinter import*
import webbrowser

# learning text

root = Tk()

text = Text(root,width = 30,height = 5)
text.pack()

text.insert(INSERT,"I love her")

text.tag_add("tag1",1.7,1.9)
text.tag_config("tag1",background = "yellow",foreground = "red")

def ShowHandCursor(event):
    text.config(cursor = "arrow")

def ShowXtermCursor(event):
    text.config(cursor = "xterm")

def Click(event):
    webbrowser.open("file:\E:\PythonLearning\Webpage55.html")

text.tag_bind("tag1","<Enter>",ShowHandCursor)
text.tag_bind("tag1","<Leave>",ShowXtermCursor)
text.tag_bind("tag1","<Button-1>",Click)

mainloop()