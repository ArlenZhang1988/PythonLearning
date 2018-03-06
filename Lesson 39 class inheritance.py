# class inheritance
import random as r

class Animal:
    def __init__(self,name):
        self.name = name
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("Axis: ( "+ self.x + " , "+ self.y + " )")

class Cow(Animal):
    pass

class Lion(Animal):
    def __init__(self,name):
        #Animal.__init__(self,name) # first way: to override parent concreate method
        super(Lion, self).__init__(name) # second way: to overide parent concreate method (recommanded)
        self.hungry = True

    def Eat(self):
        if (self.hungry):
            print(self.name + " will eat you")
            self.hungry = False
        else:
            print(self.name + " is fulled")

lion = Lion("Lion")
lion.Eat()
lion.Eat()

# mutiple inheritance
class Base1:
    def Fun1(self):
        print("Fun1 is calling")

class Base2:
    def Fun2(self):
        print("Fun2 is calling")

class TestClass(Base1,Base2):
    pass

test = TestClass()
test.Fun1()
test.Fun2()