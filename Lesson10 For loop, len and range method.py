#learning for loop same as foreatch in c#
testStr = 'Test str'
for i in testStr:
    print(i, end= ' ')

print("\n");

#learning len method in python
member = ['Happy','Shourd','Stwie2']
for i in member:
    print(i, len(i)) #in this case the len() method is equevalent to member.Length() in c#

#learning range() method
#range([start,]stop[,step = 1]). paramenter with [], means that you don't have to pass the value for it
numArr1 = range(10)
numarr2 = range(1, 11)
numarr3 = range(1, 11, 2)
for i in numArr1:
    print(i,end = ' ')
print("\n");
for i in numarr2:
    print(i,end = ' ')
print("\n");
for i in numarr3:
    print(i,end = ' ')
print("\n");