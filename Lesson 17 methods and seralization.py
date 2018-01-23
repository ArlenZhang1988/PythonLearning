# seralization

# list seralization
str = "I love you"
listSeralization = list(str)
print(listSeralization)

# tuple seralization
tupleSeralization = tuple(str)
print(tupleSeralization)

# sum method
sumTuple = (1,1,1,1)
print(sum(sumTuple))

# enumerate mehtod. Turn a data type into an enum
print(list(enumerate(sumTuple)))

# zip method. Combine two lists in a way that the elements in list1 will assoicate with all the elements in list2 as their enum index
list1 = [3,2,1,0]
list2 = [0,1,2,3]
print(list(zip(list1,list2)))
