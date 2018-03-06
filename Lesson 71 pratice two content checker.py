from tkinter import*
import hashlib

# learning checker

root = Tk()

text = Text(root,width = 30,height = 5)
text.pack()

text.insert(INSERT,"I low her")
contents = text.get("1.0",END)

def GetSig(contents):
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = GetSig(contents)

def Check():
    contents = text.get("1.0",END)

    if sig != GetSig(contents):
        print("Data is changed")
    else:
        print("Data is not changed")

Button(root,text = "Check content", command = Check).pack()

mainloop()