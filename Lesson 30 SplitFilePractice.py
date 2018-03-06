_f = open("E:\\PythonLearning\\Lesson 30 File.txt","r")

_a = []
_b = []

counter = 1

def SaveFile(filePath,count,lines):
    f = open(filePath+str(count)+".txt",'w')
    f.writelines(lines)
    f.close()

for eachLine in _f:
    if eachLine[:6] != "======":
        (role,spoken) = eachLine.split(':',1)

        if(role == "A"):
            _a.append(spoken)
        elif (role=="B"):
            _b.append(spoken)
    else:
        path = "E:\\PythonLearning\\Lesson 30 Task\\A"
        SaveFile(path,counter,_a)

        path = "E:\\PythonLearning\\Lesson 30 Task\\B"
        SaveFile(path,counter,_b)

        _a = []
        _b = []

        counter += 1

_f.close()