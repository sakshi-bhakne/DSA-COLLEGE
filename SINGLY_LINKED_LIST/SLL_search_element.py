
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

    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")


mylist = SinglyLinkedList()
mylist.insert_end(10)
mylist.insert_end(20)
mylist.insert_end(30)

mylist.search(20)
mylist.search(50)
