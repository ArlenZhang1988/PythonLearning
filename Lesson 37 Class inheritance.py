# class learning

# create a class
class Gakki:
    _race = "Yellow"
    _age = 29
    _name = "Aragaki Yui"

    def Eat(self,food):
        print (" is eating " + food)

g = Gakki()
g.Eat('Cake')

# inheritance
class MyList(list):
    pass

    def NewMethod(self):
        print("NewMethod")
# MyList is a chile class of list, pass has to be included

list = MyList()
list.append("s")
list.append('ell')
list.NewMethod()

print(list)

# 多态poly.,, 
class A:
    def Fun(self):
        print("Method in a")

class B (A):
    def Fun(self):
        print("Method in b")

a = A()
b = B()

a.Fun()
b.Fun()