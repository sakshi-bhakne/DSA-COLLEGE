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

    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            if self.head is None:
                self.head = Node(data)
                self.head.next = self.head
            else:
                new_node = Node(data)
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                new_node.next = self.head
                temp.next = new_node
                self.head = new_node
            return

        if self.head is None:
            print("Invalid position")
            return

        temp = self.head
        count = 1

        while count < pos - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        if count != pos - 1:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

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
ll.insert_position(15, 2)
ll.display()