# learning tuple

# tuple is unchangable

# create a tuple
tuple1 = (2, 3, 4, 1, 2)
print(tuple1)
print( type(tuple1))

tuple2 = (1)
print(tuple2)
print( type(tuple2))  # data type int

tuple2 = (1,)  # include a "," if you want to create a tuple which contains one element.
print(tuple2)
print(type(tuple2)) # data type tuple
tuple3 = 1,  # same as line 14
print(tuple3)
print(type(tuple3))  # data type tuple

# to change the tuple elements, you have to create a new tuple
tuple4 = (1,2,4,5)
tuple4 = tuple4[:2] + (3,) + tuple4[2:]
print(tuple4)