temp = input("Enter a number, enter -1 to exit the app.\n")
num = int(temp)

while (num != -1):
    if(num>=90):
        print("Number you enterd: " + str(num) + ".S Your grade: A \n")
    elif(80<=num<90):
        print("Number you enterd: " + str(num) + ". Your grade: B \n")
    elif(60<=num<80):
        print("Number you enterd: " + str(num) + ". Your grade: C \n")
    elif(0<=num<60):
        print("Number you enterd: " + str(num) + ". Your grade: D \n")

    temp = input("Enter a number, enter -1 to exit the app.\n")
    num = int(temp)

x,y = 4,5
small = x if x<y else y #三元操作符

assert False #assert error for testing