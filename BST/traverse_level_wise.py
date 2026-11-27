class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right
    def inorder(self,temp):
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)
    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
            return 
        arr = [rt]
        count = 0
        level = 0
        #or
        # arr.append(rt)
        while count <len(arr):
            node_count = len(arr) - count #numbers of nodes to be visited
            print("\n level: ",level,end = " ")
            for i in range(node_count):
                temp =arr[count]
                count +=1
                print(temp.data, end=" ")
            
            if temp.left:
                arr.append(temp.left)
            
            if temp.right:
                arr.append(temp.right)
        # print(count)
            level += 1
        print("\n height of the tree : ",level - 1)

            
btree = BST()
btree.insert(Node(100))
btree.insert(Node(10))
btree.insert(Node(450))
btree.insert(Node(4))
btree.insert(Node(65))
btree.insert(Node(300))
btree.insert(Node(500))
btree.insert(Node(50))
btree.insert(Node(70))

print("Inorder:")
btree.inorder(btree.root)

print("\nLevel_Order:")
btree.level_order(btree.root)


        
            