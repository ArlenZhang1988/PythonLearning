# make a timer
import time as s

class Timer:
    def __init__(self):
        self.hasStarted = False
        self.prompt = "Timer is not started"
        self.unit = ["years","months","days","hours","seconds"]

    def Start(self):
        self.timePassed = 0
        self.hasStarted = True
        self.timeStarted = s.localtime()

    def Stop(self):
        if(not self.hasStarted):
            print("Please, start the timer before you stop")
            return

        self.hasStarted = False
        self.timeStoped =  s.localtime()
        self.Calc()

    def Calc(self):
        self.timePassed = []
        self.prompt = "Time spent: "

        for index in  range(6):
            self.timePassed.append(self.timeStoped[index] - self.timeStarted[index])

            if self.timePassed[index]:
                self.prompt += str(self.timePassed[index]) + self.unit[index]

        print(self.prompt)

    def __add__(self, other):

        newPrompt = "Time spent"

        result = []

        for index in range(6):
            result.append(self.timePassed[index] + other.tiem)

        return newPrompt

    def __str__(self):
        return self.prompt

t = Timer()
t.Start()
t.Stop()