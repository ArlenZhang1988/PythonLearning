# learning list box
from tkinter import *

master = Tk()

theLb = Listbox(master,height = 25)
theLb.pack()

games = ["LoL","Counter Strike","Dota2"]

for game in games:
    theLb.insert(END,game)

b = Button(master,text = "Delete it",command = lambda x = theLb: x.delete(ACTIVE))
b.pack()

# scrollbar
sb = Scrollbar(master)
sb.pack(side = RIGHT,fill= Y)

lb = Listbox(master,yscrollcommand = sb.set)

for i in range(1000):
    lb.insert(END,i)

lb.pack(side = LEFT,fill = BOTH)

sb.config(command = lb.yview)

#scale
Scale(master,from_=  0,to = 40,tickinterval = 5, resolution = 5, length  = 200).pack()
Scale(master,from_ = 0, to = 200, orient = HORIZONTAL).pack()

mainloop()