#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.cnt = 0
       
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            # if rt.left is None and rt.right is None:
            if rt.left is not None or rt.right is not None:
                self.cnt+=1
                self.inorder(rt.right)

            
    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")
    def findminmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\nMin value: ", temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)

    def delete_node(self,rt,val):
        if rt is None:
            return rt
        if val <rt.data:
            rt.left = self.delete_node(rt.left,val)
        elif val > rt.data:
            rt.right = self.delete_node(rt.right,val)
        else:
            if rt.left is None:#node with right chile only
                return rt.right
            if rt.right is None:#node with left chile pnly
                return rt.left
            #node has both left and right children
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.delete_node(rt.right,succ.data)
        return rt
    def get_successor(self,temp):
        temp = temp.right
        while temp.left is not None :
            temp = temp.left
        return temp
    def search(self,key):#To search a perticular value.
        temp = self.root
        while temp:
            if temp.data  == key:
                return True
            elif key<temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False


b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(500))
b1.insert(Node(34))
print("\nInorder: ")
b1.inorder(b1.root)
# print("\ntotal non of left nodes: ",b1.cnt)
# print("\nPreorder: ")
# b1.preorder(b1.root)
# print("\nPostorder: ")
# b1.postorder(b1.root)
# b1.findminmax(b1.root)
b1.delete_node(b1.root,10)
print("\n after deletion: ",end = " ")
b1.inorder(b1.root)
if b1.search(4):
    print("\n Found the node")
else:
    print("\n Not found")
