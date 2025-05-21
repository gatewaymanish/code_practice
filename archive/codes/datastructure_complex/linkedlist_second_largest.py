

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def head_insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def find_second_largest(self):
        self.largest = -1
        self.second_largest = -1
        




llist = LinkedList()
llist.head_insert(33)
llist.head_insert(12)
llist.head_insert(3)
llist.head_insert(0)
llist.head_insert(88)
llist.head_insert(21)

llist.find_second_largest()