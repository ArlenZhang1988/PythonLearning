#decriptor

class MyDecriptor:
    def __get__(self, instance, owner):
        print("getting...",self,instance,owner)

    def __set__(self, instance, value):
        print("setting...",self,instance,value)

    def __delete__(self, instance):
        print("deleting....",self,instance)


class Test:
    x = MyDecriptor()

t = Test()
t.x = "X-man"
print(t.x)
del t.x

# property
class MyProperty:
    def __init__(self,fget,fset,fdel):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance,value)

    def __del__(self,instance):
        self.fdel(instance)

class C:
    def __init__(self):
        self.__x = None

    def GetX(self):
        return self.__x

    def SetX(self,value):
        self.__x = value

    def DelX(self):
        del self.__x

    X = MyProperty(GetX,SetX,DelX)

c = C()
c.X = 23
print(c.X)