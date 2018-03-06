# learning list

# Methods

# fromkeys method.
dict1 = {} # create an empty dictionary
dict1 = dict.fromkeys((1,2,3,4)) # create keys with none value
print(dict1)

dict1 = dict.fromkeys((1,2,3,4),"Test") # adding the same value to each key
print(dict1)

# Access list
dict2 = dict.fromkeys((1,2,3,4,5,6,7),"SameValue")

# keys method
counter = 1

print("Using keys method")

for i in dict2.keys():
    print(str(counter)  + ": " + dict2[i])
    counter += 1

# values method
counter = 1

print("Using Values method.")

for i in dict2.values():
    print(str(counter) + ": " + i)
    counter += 1

# items method. Return a list of items(key and value)
print("Using items method.")

for i in dict2.items():
    print(i)

# get method. If you are trying to access a key which is not in the dict this method will return none value
gettedValue = dict2.get(555)
print(type(gettedValue))

# pop method. Return a value according to the key you entered and then deleted the item in the list
print(dict2.pop(2))
print(dict2)

# Delete items

#clear method.
dict2.clear();
print(dict2)

# Add item

#setDefault method.
dict2.setdefault("Arlen") # setDefault(p), p is a key which doesn't have to be in the list, if the p is not in the list, the list will create a new item with key p and value none
print(dict2)
dict2.setdefault("Gakki","Cute") #setDefault(p1,p2),if p2 is passed to the method, the new item holds value of p2 with key p1
print(dict2)

# Change value

# update method. update(p), p is a list. List which is calling this method will overwrite the value in p.
dict3 = {"Arlen":"Daddy"}
dict2.update(dict3)
print(dict2)
