# document method

# document content shoube be prefixed and suffixed with triple double-quotes
def DocumentMethod():
    """Document"""
    print('what?')


DocumentMethod()
print(DocumentMethod.__doc__)

# keyword-prefixed parameter. Use the parameter name and "=" symbol when calling the method
def Proverb(name, str):
    print(name + ": " + str)


Proverb("项羽","力拔山兮气盖世，时不利兮骓不逝。")
Proverb("力拔山兮气盖世，时不利兮骓不逝。","项羽")
Proverb(str = "力拔山兮气盖世，时不利兮骓不逝。", name = "项羽")

# default parameter. Include a value for parameter when creating the method
def Proverb(name = "Daddy", str = "Hello"):
    print(name + ": " + str)


Proverb()