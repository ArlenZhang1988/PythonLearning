# concreate and 解析方法
class A:
    def __init__(self):
        print("Calling init method")
    def __del__(self):
        print("Calling del method")

a = A()

# override operator
class Potion:
    def __init__(self):
        self.count = 1

    def __add__(self, other):
        return
    def __sub__(self, other):
        return
    pass
