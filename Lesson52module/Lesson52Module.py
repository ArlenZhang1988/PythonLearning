def MyGen():
    print("yield")
    yield 1
    yield 2

def Test():

    print("Testing Module 52")

    gen = MyGen()

    # for
    for each in gen:
        print(each)

# Test will be called when importing this module without this if statement
if __name__ == "__main__":
    Test()