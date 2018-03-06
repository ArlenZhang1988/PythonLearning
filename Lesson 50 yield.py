# yield.
def MyGen():
    print("yield")
    yield 1
    yield 2

gen = MyGen()

# for
for each in gen:
    print(each)

# Fib practice
def Libs():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a

for each in Libs():
    if each > 100:
        break

    print(each, end = " ")

#
a = [i for i in range(100) if not(i % 2) and i % 3]
for each in a:
    print(each, end = " ")

print("\n")

b = {i:i % 2 == 0 for i in range(10)}
print(b)