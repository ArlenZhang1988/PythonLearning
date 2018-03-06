#file operations in python

#load file
f = open('E:\\PythonLearning\\Lesson 29 File.txt', 'r')  #open(p1,p2). p1 is the file path '\' has to be stored as a symbol in the stirng, p2 is the file mode which is 'r' in default
                                                         #  'r' = read only 'a' = writeable file
print(f)

# write file
#f = open('E:\\PythonLearning\\Lesson 29 File.txt', 'a')
#f.write('Test')

# read file
#f = open('E:\\PythonLearning\\Lesson 29 File.txt', 'r')
#print(f.read(4))

# read a line
#print(f.readline())

# file to list
#print(list(f))

# print file
for eachLine in f:
    print(eachLine)