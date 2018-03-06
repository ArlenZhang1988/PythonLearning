# Build-in functions

# issubclass(p1,p2). p1 and p2 are both class name
class A:
    pass

class B(A):
    pass

print(issubclass(B,A))
print(issubclass(B,B)) # In python, every class is considered as child class of itself.
print(issubclass(B,object))

# isinstance(p1,p2). p1 is the instance name, p2 is the class(you can pass set through p21)
a = A()
b = B()

class C:
    pass

c = C()

print(isinstance(a,A))
print(isinstance(b,A))
print(isinstance(c,A))

# hasattr(p1,p2). p1 is the instance or class name, p2 is the attribute name (use " ")
class D:
    def __init__(self):
        self.x = 1

d = D()
print(hasattr(d,"x"))

# getattr(p1,p2). p1 is the instance name, p2 is the attribute name (use " ")
d = D()
print(getattr(d,"x"))

# setattr(p1,p2,p3). p1 is the instance name, p2 is the attribute name (use " "),p3 is the new value for p2
setattr(d,"x",2)
print(getattr(d,"x"))

# delattr(p1,p2). p1 is the instance name, p2 is the attribute name(use "")
delattr(d,"x")
print(hasattr(d,"x"))

# property(p1,p2,p3). p1 is the method to return variable, p2 is the method to set variable, p3 is the method to delete variable
class E:
    def __init__(self):
        self.__size = 20

    def SetSize(self,size):
        self.__size = size

    def GetSize(self):
        return self.__size

    def DelSize(self):
        del self.__size

    Size = property(GetSize,SetSize,DelSize)

e = E()
print("\n"+ str(e.Size))
e.Size = 10
print(e.Size)
del e.Size
print(hasattr(e,"Size"))