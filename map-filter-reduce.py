# MAP

def cube(x):
    return x*x*x

lis1 = [1,3,5,7,9]

# lets say i want the cube of everyelement as a list

# approach 1 - 
def app1():
    newL = []
    for i in lis1:
        newL.append(cube(i))
    print(newL)

app1()

# approach 2 - 
def app2():
    return list(map(cube,lis1)) # map is used for complexity purposes and conviniency

print(app2())

# FILTER 

# it is filters the elements based on the condition and return the filtered elements.

def filter_function(a):
    return a>4

dd =  list(filter(filter_function, lis1))
print(dd)


# REDUCE

from functools import reduce

ddd= reduce(lambda x,y:x+y, lis1)
print(ddd)