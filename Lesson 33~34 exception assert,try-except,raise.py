 # debug in python

# using assert
map = ['She is cute']
assert (len(map)>0)
map.pop()
#assert (len(map)>0)

# using try-except
try:
    1/0
    sum = 1+"1"
except TypeError as reason: # according to the error type
    print("Type error: "+ str(reason))
except: # despite anytype of error. Not recommand
    print("Error occurs")
finally: # run the codes even though there is an error occurs
    print("Print after error occurs")

# using raise to print an error directly
raise TypeError("Similar to debug.log in unity")