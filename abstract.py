from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        pass

class Rectangle(Shape):
    sides = 4

    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle(6,7)
# print(rect1.printarea())


## The class Shape is an abstract class from which Rectangle Class inherits the properties of theSha[ppe class.


### Property decorators - setters and getters and deleters

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @property
    def explain(self):
        return f"This employee name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname is None and self.lname is None:
            self.email = "The email is not set"
        return f"{self.fname.lower()}.{self.lname.lower()}@bonamisoftware.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname =None


nilabh_sahu = Employee("Nilabh","Sahu")
keshar_jha = Employee("Keshar","Jha")

print(nilabh_sahu.email) # here, we called the function "explain" as an attribute method

# now if we wamt to set the attribute of the class, we can use setter

nilabh_sahu.email = "this.that@gmail.com"
print(nilabh_sahu.fname)

# if we were to delete a attribute property, we use deleter

del nilabh_sahu.email