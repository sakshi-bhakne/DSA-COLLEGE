
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

    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)


mylist = SinglyLinkedList()
mylist.insert_end(10)
mylist.insert_end(20)
mylist.insert_end(30)
mylist.insert_end(40)
mylist.insert_end(50)

mylist.find_middle()
