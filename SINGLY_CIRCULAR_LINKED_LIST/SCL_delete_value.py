class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def delete_value(self, key):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("back to head")


ll = SinglyCircularLinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.delete_value(20)
ll.display()