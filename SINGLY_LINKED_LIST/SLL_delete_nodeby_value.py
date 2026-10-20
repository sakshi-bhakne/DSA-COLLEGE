
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

    def delete_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Element not found")

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

mylist.delete_value(20)
mylist.display()
