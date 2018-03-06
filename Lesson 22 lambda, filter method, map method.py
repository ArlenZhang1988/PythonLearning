# learning lambda

square = lambda x : x * x
print(square(2))

add = lambda x, y: x + y
print(add(1,2))

#filter method. filter(p1,p2), p1 could be None or method, p2 is a list
filter(None,[1,0,False,True]) # this method will return all True value in p2
print(list(filter(None,[1,0,False,True])))

# odd number filter
def odd(x):
    return x%2 != 0

print(list(filter(odd,[1,2,3,4,5,6,7,8,9])))

tempList = filter(lambda x: x % 2 != 0,[1,2,3,4,5,6,7,8,9]) # using lambda instead of method
print(list(tempList))

# map method, just like foreach in c#. map(p1,p2), p1 is the operation to the value, p2 is the list of values
print(list(map(lambda x: x *2,range(10))))