
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Display
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 2. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 4. Insert at position (1-based)
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_beginning(data)
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

    # 5. Search
    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                print("Element found")
                return
            temp = temp.next

        print("Element not found")

    # 6. Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Total nodes:", count)

    # 7. Delete beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # 8. Delete end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # 9. Delete by value
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

    # 10. Reverse
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 11. Find middle
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

    # 12. Sum of nodes
    def sum_nodes(self):
        total = 0
        temp = self.head

        while temp is not None:
            total += temp.data
            temp = temp.next

        print("Sum:", total)


# Main program
mylist = SinglyLinkedList()

mylist.insert_end(10)
mylist.insert_end(20)
mylist.insert_end(30)

print("Original list:")
mylist.display()

print("Insert at beginning:")
mylist.insert_beginning(5)
mylist.display()

print("Insert at position 3:")
mylist.insert_position(15, 3)
mylist.display()

mylist.search(20)
mylist.count_nodes()
mylist.find_middle()
mylist.sum_nodes()

print("Delete first node:")
mylist.delete_beginning()
mylist.display()

print("Delete last node:")
mylist.delete_end()
mylist.display()

print("Delete value 20:")
mylist.delete_value(20)
mylist.display()

print("Reverse list:")
mylist.reverse()
mylist.display()
