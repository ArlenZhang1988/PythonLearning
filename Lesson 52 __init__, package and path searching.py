
# import python module from folder
import sys

sys.path.append("E:\PythonLearning\Lesson52module")

# learning __name__ = "__main__"
import Lesson52Module as l

gen = l.MyGen()

for each in gen:
    print(each)

# using package
# 1: create a new folder
# 2: create a file call __init__.py inside that folder
# 3: drag all the modules into that folder
import Lesson52module.Lesson52Module as l # 4: use folder name + "." + module name to import module

gen = l.MyGen()

for each in gen:
    print(each)