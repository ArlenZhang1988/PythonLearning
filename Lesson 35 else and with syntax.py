# else syntax in python

# else with try-except
try:
    9/1
    #1/0
except ZeroDivisionError:
    print("Happy Log")
else: # if except is call then else will not be called.
    print("No error occurs")

# with syntax
# using with syntax, the file you opened will automatically close when it is no longer needed
with open('E:\\PythonLearning\\Lesson 29 File.txt', 'r') as f:
#operations
