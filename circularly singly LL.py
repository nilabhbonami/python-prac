class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next

class CircularlyLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print ("List empty")
            return

        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag:
            print (temp.data)
            temp = temp.next
        return

    def add_node(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            return

        curr = self.head
        first = self.head
        while curr.next != first:
            curr = curr.next
            curr.next = first
        return

ll = CircularlyLinkedList()
ll.add_node(5)
ll.display()