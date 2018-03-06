# learning class

class Test:

    name = "lol"

    def __init__(self,name): # concreate method
        self.name = name

    def YouNameIs(self,name): # use self to set the variable in this class
        self.name = name

    def Kick(self):
        print("Kick " + self.name)

test = Test("xD")
test.Kick()
test.YouNameIs("Right")
test.Kick()

# private and public variable
class Animal:
    name = "Cow"
    __age = 13 # use "__" to make variable a private one

    def PrintAge(self):
        print(self.__age)

a = Animal()
print(a.name)
a.PrintAge()

print(a._Animal__age) # using format _ClassName__VariableName