# learning set
# set doesn't contain repetitive values

# create
set1 = {1,2,3,45,6,1,2,6}
print(type(set))
print(set)

num1 = [1,2,3,4,5,6,7,1,2,5,3,7,8]
set2 = set(num1)
print(set2)

# add value
set2.add(99)
print(set2)

# delete value
set2.remove(99)
print(set2)

# unchangeable set
set2 = frozenset(num1)
print(set2)