# learning module. imilar to namespace in c#

# import whole module as an instance (recommanded)
import Lesson51Module as l

gen = l.MyGen()

for each in gen:
    print(each)

# import methods from a module
from Lesson51Module import MyGen

gen = MyGen()

for each in gen:
    print(each)