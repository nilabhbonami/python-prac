# 2. Doubly Linked List

class newNode:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def add_node(self,data): # in the end
        new_Node = newNode(data) # if head is empty then we will point the head and tail both to the new node
        if self.head is None:
            self.head = new_Node
            self.tail = self.head
            return
        else: #Else, we make the previous pointer of the new node point to the present tail.
            new_Node.prev = self.tail
            self.tail.next = new_Node # we make next pointer of the present tail point to the new node thus establishing a 2 way connection between the present tail and new node
            self.tail = new_Node
            return

    def add_beg(self,data):
        new_Node = newNode(data)
        new_Node.next = self.head
        new_Node.prev = None

        if self.head is not None:
            self.head.prev = new_Node
        self.head = new_Node

    def add_end(self,data):
        new_Node = newNode(data)
        if self.head is None:
            new_Node.prev = None
            self.head = new_Node
            return
        curr = self.head
        new_Node.next = None
        while curr.next is not None:
            curr = curr.next
        curr.next = new_Node
        new_Node.prev = curr

    def insert_after(self,prev_node, data):
        if prev_node is None:
            print("The node doesn't exist")
            return
        new_Node = newNode(data)
        new_Node.next = prev_node.next
        prev_node.next = new_Node
        new_Node.prev = prev_node
        if new_Node.next is not None:
            new_Node.next.prev = new_Node

    def add_before(self,given_node,data):
        if given_node is None:
            print("Node doesn't exists")
            return
        new_Node = newNode(data)
        new_Node.prev = given_node.prev
        given_node.next = new_Node
        new_Node.next = given_node
        if new_Node.prev is not None:
            new_Node.prev.next = new_Node


    def print_list(self):
        if self.head is None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, '-->',end= '')
                current_node = current_node.next
        print('End of list')


ll = DoublyLinkedList()
ll.add_node(5)
ll.add_node(10)
ll.add_beg(12)
ll.add_end(15)
# ll.insert_after(11,3)
# ll.add_before(15,11)
ll.print_list()




