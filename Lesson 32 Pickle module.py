# learning pickle module similar to serialize file in c#?

import os
import pickle

#os.mkdir(os.curdir+"\Lesson 32 Folder")

# create a pickle file which is a binary file
listToBeSaved = [1,"Aragaki Yui",[1988,6,1],True]
file = open(os.curdir+"\Lesson 32 Folder"+"\listToBeSaved.pkl","wb" ) #  Use pkl as suffix for p1, p2 has to be wb.
pickle.dump(listToBeSaved,file)
file.close()

# load a pickle file
file = open(os.curdir+"\Lesson 32 Folder"+"\listToBeSaved.pkl","rb" ) #  Up2 has to be rb.
listToStoreItem = pickle.load(file)
print(listToStoreItem)
file.close()