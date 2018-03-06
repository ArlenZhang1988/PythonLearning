# protocol

class CounterList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

c1= CounterList(1,2,3,4)
c2 = CounterList(5,6,7,8)

print(len(c1))
print(c1[2])
print(c1.count)
print(c1[1])
print(c1.count)