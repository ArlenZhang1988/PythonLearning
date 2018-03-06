#learning method nesting

# method nesting
def f1():
    print("f1 is called")
    def f2():
        print("f2 is called")
    f2()

f1()

# method closure
def funx(x):
    def funy(y):
        return x*y
    return funy;

returnFunction = funx(8) # called the funx function which will return funy function
print(type(returnFunction)) # returnFunction holds an funy function pointer
print(returnFunction(2)) # call the funy funtion
print(funx(8)(2)) # call the funx and funy method at the same time.

# local variable in nesting method
def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return x

print(fun1())