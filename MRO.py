class A:
    def display(self):
        print("Class A method")

class B:
    def display(self):
        print("Class B method")

class Example(B,A):
    def show(self):
        print("Class Example Method")


inst = Example()
inst.display()  

## MRO ## Class Example ---> Class B ---> Class A


########  Approach 1  #########


# def practice():
#     with open("story.txt","r") as file:
#         count=0
#         for line in file:
#             if line[0] not in 'T':
#                 count+= 1
#     print(count)

# practice()


########  Approach 2  #########

def practice():
    with open("story.txt","r") as file:
        count = sum(line[0] not in 'T' for line in file)
    print(count)

practice()