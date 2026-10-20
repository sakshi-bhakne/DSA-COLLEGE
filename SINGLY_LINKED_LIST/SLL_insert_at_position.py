
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


mylist = SinglyLinkedList()
mylist.insert_end(10)
mylist.insert_end(20)
mylist.insert_end(30)

mylist.insert_position(25, 3)
mylist.display()
