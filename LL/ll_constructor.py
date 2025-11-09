class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LindedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linked_list = LindedList(4) 
print(my_linked_list.head.next)