# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right

    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)


# Main program
b = BST()

b.insert(Node(50))
b.insert(Node(30))
b.insert(Node(70))
b.insert(Node(20))
b.insert(Node(40))
b.insert(Node(60))
b.insert(Node(80))

print("Inorder Traversal:")
b.inorder(b.root)