class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    def pop(self):
        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            
    
    def print(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.value}-> ", end="")
            temp = temp.next
    
my_linked_list = LinkedList()
my_linked_list.length = 0
for i in range(1,6):
    my_linked_list.length += 1
    my_linked_list.append(i)
    my_linked_list.print()
    print("\n")
