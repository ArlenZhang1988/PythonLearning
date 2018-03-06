from tkinter import *

# check button
root = Tk()

answers = ["Gki","Gakki","Kimy","Loky"]

v = []

for answer in  answers:
    v.append(IntVar())
    b = Checkbutton(root,text = answer)
    b.pack(anchor = W)

# label frame
group = LabelFrame(root,text ="Langage used in Unity?",padx = 10, pady = 5)
group.pack(padx = 10, pady = 10)


# radio button
lanages = [
    ("C#",1),
    ("Java", 2),
    ("Python",3),
    ("Html",4)
]

v = IntVar()
v.set(1)

for lang,num in lanages:
    b = Radiobutton(group,text = lang,variable = v, value = num)
    b.pack(anchor = W)


mainloop()