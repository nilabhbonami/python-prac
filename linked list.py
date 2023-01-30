# 1. Array
# 2. Linked List
# 3. Trees
# 4. Graphs
# 5. Hashmap
# 6. Trie
# 7. Stack and Queue

# x - value, i - index
#### Arrays - pop, remove(x), append, insert(i, x), index, reverse 
    
import array

arr = array.array('i',[1,2,3,4,5,6,310])
# for i in arr:
#     print(i) 
arr.remove(310)
#print(arr)




###### Linked List #######
# 1. Singly Linked List

class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self,data):
        new_Node = Node(data)
        self.head = new_Node

    def add_last(self,data):
        new_Node = Node(data) # create a new node
        if self.head is None: # if the linked list is empty
            self.head = new_Node # assign new node to it
            return
        else:
            current = self.head
            while current.next is not None: # move to the last node of the list
                current = current.next
            # point the last node of the list to the new node so that new node gets added to the end of the list
            current.next = new_Node

    def add_beg(self,data): # adding a node at the beginning
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def del_beg(self):
        current = self.head
        if current is None:
            print("Linked List Underflow !!")
        self.head = current.next

    def del_last(self):
        current = self.head
        prev = None
        if current is None:
            print("No head element !!")
        else:
            while current.next is not None:
                prev = current
                current = current.next

            if prev is None:
                self.head = None
            else:
                prev.next = None

    def print_data(self):
        current = self.head
        while current is not None:
            print(current.data, '-->', end='')
            current = current.next
        print('End of list')


ll = LinkedList()
ll.add_first(10)
ll.add_beg(5)
ll.add_beg(4)
ll.add_beg(3)
ll.add_last(12)
ll.add_last(15)
ll.print_data()
ll.del_beg()
ll.print_data() # 3 is deleted from the beginning of the list
ll.del_last()
ll.print_data()


