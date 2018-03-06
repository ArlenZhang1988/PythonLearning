from tkinter import*

# learning how to bind event
root = Tk()

frame = Frame(root,width = 200,height = 200)

def MouseCallBack(event):
    print("Click: ",event.x,event.y)

def KeyboardCallBack(event):
    print(event.char)
    print(event.keysym)

def MouseMotion(event):
    print("Click: ",event.x,event.y)

frame.bind("<Button-1>",MouseCallBack) # mouse event
frame.bind("<Key>",KeyboardCallBack) # keyboard event
frame.bind("<Motion>",MouseMotion) # mouse motion
frame.focus_set()
frame.pack()

mainloop()