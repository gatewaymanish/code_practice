

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def search(self, value):
        node = self.head
        while node is not None:
            if node.data == value:
                print('found')
                break
            elif node.next is None:
                print('not found')
            node = node.next

    def head_insert(self, new_data):
        first_node = self.head
        new_node = Node(new_data)
        new_node.next = first_node
        self.head = new_node
        print('inserted ', new_data, ' at begining')

    def tail_insert(self, new_data):
        node = self.head
        while node is not None:
            if node.next is None:
                break
            node = node.next
        new_node = Node(new_data)
        node.next = new_node
        print('inserted ', new_data, ' at end')

    def delete_node(self, remove_data):
        node = self.head
        while node is not None:
            if node.next.data == remove_data:
                break
            node = node.next
        node.next = node.next.next


n1 = Node('mon')
list = LinkedList()
list.head = n1

n2 = Node('tue')
n1.next = n2

n3 = Node('wed')
n2.next = n3

n4 = Node('thur')
n3.next = n4

n5 = Node('fri')
n4.next = n5


# list.search('mon')
list.head_insert('helloo')
list.tail_insert('bye')
list.delete_node('wed')
list.print_all()