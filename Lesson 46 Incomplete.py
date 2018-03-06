# __setattr(p1,p2). p1 is the attr name, p2 is the value

class A:
    def __init__(self):
        self.x = 10

    def __setattr__(self, name, value):
        if (name == "Test"):
            self.x = value

a = A()
a.Test = 10
print(a.x)