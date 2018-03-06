# composition

class Turtle:
    def __init__(self,num):
        self.num = num

class Fish:
    def __init__(self,num):
        self.num = num

class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def PrintX(self):
        print("There are %d turtles and %d fishes in the pool." %(self.turtle.num, self.fish.num))

p = Pool(2,10)
p.PrintX()

# class, class instance
class C:
    count = 0

a = C()
b = C()
c = C()

a.count += 10 # a.count is a local variable
print("A: "+str(a.count) + " " + "B: "+str(b.count) + " " + "C: "+str(c.count))

C.count = 100 # C.count is a static variable
print("A: "+str(a.count) + " " + "B: "+str(b.count) + " " + "C: "+str(c.count))

# override method with variable
class C:
    def X(self):
        print("x")

d = C()
d.X()
d.X = 1
print(d.X)