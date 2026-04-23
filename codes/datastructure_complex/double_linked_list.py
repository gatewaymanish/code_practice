
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        """Traverse and print the list forward."""
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        """Traverse and print the list backward."""
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Usage Example
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.display_forward()  # Output: 10 <-> 20 <-> 30 <-> None
dll.display_backward() # Output: 30 <-> 20 <-> 10 <-> None