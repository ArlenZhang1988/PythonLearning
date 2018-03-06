# iterator

# use iterator
link = {"Hi","Yup","No"}

for each in link:
    print(each)

# use iter and next method
it = iter(link)
print(next(it))
print(next(it))
print(next(it))

# __iter__() and __next()
# fib pratice
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

fibs = Fibs()
it = iter(fibs)

for index in range(7):
    print(next(it))