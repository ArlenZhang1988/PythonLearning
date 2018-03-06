# return type and method

# every method in python return a value which is a none type value
def NoneReturnTypeMethod():
    print("No return type here")

temp = NoneReturnTypeMethod()
print(temp)
print(type(temp))

# method with return type
def ReturnTypeMethod():
    return 25

temp  = ReturnTypeMethod()
print(temp)

#local variable and global variable
def Discount(prize = 25, rate = 0.9):
    finalPrize = prize* rate
    print("Called from discount method: "+ str(enteredPrize))
    enteredPrize - 80 #the discount method created a new local variable with same name of this global variable
    print("Print after changing the value enteredPrize in discount method: " + str(enteredPrize))
    return finalPrize

enteredPrize = 100
print(Discount(enteredPrize,0.25))
#print(finalPrize) #error occurs, finalPrize is an local vairbale
print("Print after calling the discoutn method: " + str(enteredPrize)) #the enteredPrize remain 100 because method can not change the global variable without global keyword