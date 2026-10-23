
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Check whether list is empty
    def is_empty(self):
        return self.head is None

    # 2. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # 3. Insert at end
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

    # 4. Insert at a position (positions start at 1)
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_beginning(data)
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

    # 5. Display all nodes
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

        print("(back to head)")

    # 6. Count nodes
    def count_nodes(self):
        if self.head is None:
            return 0

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        return count

    # 7. Search for a value
    def search(self, key):
        if self.head is None:
            return False

        temp = self.head

        while True:
            if temp.data == key:
                return True

            temp = temp.next

            if temp == self.head:
                break

        return False

    # 8. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head

        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head

    # 9. Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # 10. Delete a node by value (first matching node)
    def delete_value(self, key):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == key:
            self.delete_beginning()
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

    # 11. Delete at a position
    def delete_position(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return

        if pos == 1:
            self.delete_beginning()
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

    # 12. Update a value
    def update(self, old_value, new_value):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            if temp.data == old_value:
                temp.data = new_value
                return

            temp = temp.next

            if temp == self.head:
                break

        print("Value not found")

    # 13. Reverse the list
    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return

        old_head = self.head
        prev = self.head
        curr = self.head.next

        while curr != old_head:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev

    # 14. Find the middle node
    def find_middle(self):
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        return slow.data


# Testing all operations
ll = SinglyCircularLinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.display()

ll.insert_beginning(5)
ll.display()

ll.insert_position(15, 3)
ll.display()

print("Total nodes:", ll.count_nodes())
print("Search 20:", ll.search(20))
print("Middle node:", ll.find_middle())

ll.update(15, 25)
ll.display()

ll.delete_beginning()
ll.display()

ll.delete_end()
ll.display()

ll.delete_value(20)
ll.display()

ll.delete_position(2)
ll.display()

ll.reverse()
ll.display()
