import random

answer = random.randint(0,10);

guess = -1
count = 0;

while (guess!=answer) and (count !=3):
        temp = input("Please guess a number between 0~10.\n")
        guess = int(temp)

        if(guess>answer):
            print("Make a smaller guess.\n")
        else:
            print("Make a greater guess.\n")

        count += 1

if(count == 3):
    print("You have wasted too many changes, the correct answer is: "+ answer)
else:
    print("You are right, the answer is: " + answer)