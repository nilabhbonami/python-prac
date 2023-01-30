# creation of lists 

# # # lisA = list()
# # # lisB = [1,2,3,3,4,5,5,5,5,"a",'b','c']
# # # print(lisB)

# # # # set

# # # b = set(lisB)
# # # print(b)

# # # # tuple

# # # t = tuple(lisB)
# # # print(t)

# # # # dictionary 

# # # d={}

# # # d[1] = 'One'
# # # d['a'] = 'apple'
# # # print(d)

""" 
# error Handling - 2 types of error 
# 1. syntax errors - program will stop the execution
# 2. Exceptions - Errors occured at the runtime. Ex - ZeroDivisionError
# """


# try and except blocks in python to handle the errors ans exceptions

try:
    print("Entered the try block")
    print(1/0)
except:
    print('This is printed because there is an exception in the try block')
else:
    print("This is printed because code in try block haven't raised any exception")
finally:
    print('This code will be printed no matter what')

# Operators ---
# 1. Arithmetic operators - +, -, *, %
# 2. Comparison operators - =, ==, <,>
# 3. Logical operators - and, or, not
# 4. Bitwise operators - &, |, ~, ^, >>, <<
# 5. Assignment operators - =, +=, *=
# 6. Identity operators - is, is not
# 7. Membership operators - in, not in


# This code runs only in python 3.10 or above versions
def number_to_string(argument):
	match argument:
		case 0:
			return "zero"
		case 1:
			return "one"
		case 2:
			return "two"
		case default:
			return "something"


argument = 2
print(number_to_string(argument))

# Loops in Python

# 1. while
# 2. for

# Shallow copy and deep copy -

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]

# using copy to shallow copy
li2 = copy.copy(li1)

# using copy to deep copy
li3 = copy.deepcopy(li1)


print ("The original elements before deep copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")


li3[2][0] = 7
print ("The new list elements after deep copying")
for i in range(0,len( li1)):
	print (li3[i],end=" ")


print ("The original elements after deep copying")
for i in range(0,len( li1)):
	print (li1[i],end=" ")

print('\r')

idd = ''
def functi():
    global idd
    print(idd)
    idd = 'Nilabh'
    print(idd)

functi()

# file handling

# f = open("/home/ctp/Bonami/file3.txt",'a+')
# f.write("This line is added while learning file handling in python")
# f.close()

f = open("/home/ctp/Bonami/file3.txt",'r')
data = f.read()
print(data)
# for word in data.split():
#     print(word)










############ Object Oriented Programming ############

# 1. Class - Class is a collectin of objects. It serves as the blueprint from which all the other objects are created.
# 2. Objects - object is an instance of a class.
# 3. Inheritance - It is the capability of one class to derive or inherit the properties from other classes.
# 4. Polymorphism - It simply means having many forms.
# 5. Encapsulation - Wrapping up the data within 1 single unit.
# 6. Abstraction - It is the hiding of unnecessary details from the users.

class Dog:
    atrr1 = 'Loyal'

    def __init__(self,name):
        self.name =name

    def speak(self):
        print(f"My name is {self.name}")

tommy = Dog('Tommy')
YoYo = Dog('YoYo')

print(f"Rodger is a {tommy.__class__.atrr1} dog")
print(f"YoYo is a {YoYo.__class__.atrr1} dog")

print(tommy.speak())



class Person:
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"Idnumber is {self.idnumber}")

class Employee(Person):
    def __init__(self, name, idnumber,salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name,idnumber)

    def details(self):
        print(f"My name is {self.name}")
        print(f"Idnumber is {self.idnumber}")
        print(f"Post is: {self.post}")

a = Employee('Nilabh',200531,1000,'Trainee')

a.display()

## passing function as a arguemnt
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func('Hi, How are you ?')
    print(greeting)

greet(shout)

# returning function from another function

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))

# Decorators - Decorators are used to modify the behaviour of the function or class.
## It this, functions are taken as the argument into another function and then called inside the wrapper function.

def decorator_func(func):
    def inner_func():
        print('This is before function execution')
        func()
        print('This is after function execution')

    return inner_func


@decorator_func
def inside_func():
    print('This is inside the function !!')


def hello_decorator(func):
    def inner1(*args,**kwargs):
        print('before execution')
        returned_value = func(*args,**kwargs)
        print('After Execution')

        return returned_value
    return inner1


@hello_decorator
def main_func(a,b):
    print('Inside the function !!')
    return a + b

a,b = 1,2
print(main_func(a,b))


def decor1(func):
    def inner():
        x = func()
        return x*x
    return inner

def decor2(func):
    def inner():
        x= func()
        return 2*x
    return inner

@decor1
@decor2
def num():
    return 3

@decor2
@decor1
def num2():
    return 3

print(num())
print(num2())



# List = []
# for character in 'Geeks 4 Geeks!':
#     List.append(character)
#     print(List)

List = [character for character in 'Geeks 4 Geeks'.split(' ')]
print(List)


# list comprehension

lis = [num for num in range(100) if num%5 ==0 if num%10 ==0]
print(lis)

lis1 =[i**2 for i in range(1,11)]
print(lis1)

# Lambda function to print the table of 10

Lis = list(map(lambda i:i*10, [i for i in range(1,11)]))
print(Lis)

def add(x,y):
    return x+y