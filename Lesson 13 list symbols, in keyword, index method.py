# learning list comparison and other keyword

# symbols
# "<" symbol. The result is the fitst comparision between two list.
list1 = [112,888]
list2 = [999,0]
print(list1>list2)  #false. Because 112 is less than 999, althrough the list1 has graeter number in index 2 compare to list2

# "+" symbol. Combine two lists, notice that the first and the second data has to be the same type.
list3 = list1 + list2
print(list3)
# list4 = list1+"225" error occurs

# "*" symbol. Duplicate all the elements in the list for number of times
list3 *= 3
print(list3)

# keywords
# in and not in keyword.
print(112 in list3)  # true.
print(112 not in list3)  # false
list4 = [["xd"], 1, 2, "Arlen"]
print("xD" in list4)  # false. this keyword doesn't loop throught the list inside a list
print(list4[0][0])  # true. You can use indexrs to find the element inside a list.

# methods in list
# index. return the index of an element
member = ["Arlen","Aweson","Lovely","You look cute"]
print(member.index("Arlen"))
