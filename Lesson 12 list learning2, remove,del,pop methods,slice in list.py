#learning list

member = ["Arlen","Aweson","Lovely","You look cute"]
#learning methods

#remove method in list
member.remove("Arlen")
print(member)

#del method
del member[1]
print(member)
#del member #the whole list is deleted
#print(member)

#pop method in list
lastMember = member.pop() #return the last element in the list, same as pop method in c# stack
print(member)
print(lastMember)

member = ["Arlen","Aweson","Lovely","You look cute"]
#list slice using listName[parameter1:parameter2]. Create a new list with elements from listName parameter1 to listName parameter2-1
cuttedList1 = member[1:2] #elements from the 1 index to 1
cuttedList2 = member[:2] #elements from the 0 index to 1
cuttedList3 = member[1:] #elemnts from the 1 index to the last index
print(cuttedList1)
print(cuttedList2)
print(cuttedList3)