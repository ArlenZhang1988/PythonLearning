import tkinter as tk

# creating root window
app = tk.Tk()
app.title("Lesson 65 Tkinter")

# adding label
theLabel = tk.Label(app,text = "GUI window lesson 65") # tkinter.Label(p1,p2). p1 = root window, p2 = label text content
theLabel.pack() # rearrange this component

# open window
#app.mainloop()

# second demo

import tkinter as tk

class APP:
    def __init__(self,master):
        frame = tk.Frame(master)
        frame.pack(side = tk.LEFT,padx = 10) # side = use enum LEFT RIGHT TOP BUTTOM to change the position of frame, padx = padding in x axis

        # creating a button
        self.hi_there = tk.Button(frame,text="Hi there",fg = "blue",command = self.ButtonEvent) # p1 = root window, text = label text content, fg = font color, command = button event, bg = background color
        self.hi_there.pack()

    def ButtonEvent(self):
        print("Hi there, this is lesson 65 button.")
root = tk.Tk()
app = APP(root)

root.mainloop()