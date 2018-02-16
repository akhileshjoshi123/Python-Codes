'''

Given two binary trees, imagine that when you overlay one on top of the other, some nodes
of the two trees are overlapped while the others are not.
Merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.


'''



class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def in_order(self):
        if self.left:
            self.left.in_order()
    
        print(self.data)
    
        if self.right:
            self.right.in_order()    
        

def mergeTrees(a, b):
 
    # 1. Both empty
    if a is None :
        return b
    
    if b is None:
        return a
    
    a.data = a.data + b.data
    
    a.left = mergeTrees(a.left,b.left)
    a.right = mergeTrees(a.right,b.right)
    
    return a
    


# Driver program to test identicalTress function
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.left.left = Node(5)



root2 = Node(2) 
root2.left = Node(1)
root2.right = Node(3)
root2.left.right = Node(4)
root2.right.right =Node(7)


tree = mergeTrees(root1, root2)

l = []
l = tree.in_order()

print(tree.in_order())
#print(l[])