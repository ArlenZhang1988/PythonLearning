aStr = "xD"
anInt = 1988
aFloat =  0.1988
aBool = True

#type return data type
print(type(aStr))
print(type(anInt))
print(type(aFloat))
print(type(aBool))

#isinstance test data type (p1,p2). p1 is a data instance, p2 is a data type for example: int, float, str, bool etc.
#if the p1 has the same data type as we passed in the p2, return true otherwise return false.
print(isinstance(aStr,int))
print(isinstance(aStr,str))