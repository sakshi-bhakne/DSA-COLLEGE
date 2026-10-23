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


ll = SinglyCircularLinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
print("Total nodes:", ll.count_nodes())