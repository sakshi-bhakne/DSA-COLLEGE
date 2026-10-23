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

    def delete_position(self, pos):
        if self.head is None or pos < 1:
            print("Invalid position or empty list")
            return

        if pos == 1:
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
        count = 2

        while curr != self.head and count < pos:
            prev = curr
            curr = curr.next
            count += 1

        if curr == self.head:
            print("Invalid position")
            return

        prev.next = curr.next

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
ll.delete_position(2)
ll.display()