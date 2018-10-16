"""
Find the diameter of a binary treeHere the diameter is maximum number of nodes possible in the tree, formed by two leaf nodes.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left),height(node.right))

def diameter(root):
    if root is None:
        return 0

    lheight = height(root.left)
    #print("Left Height of ",root.left," is ",lheight)
    rheight = height(root.right)
    #print("Right Height of ",root.right," is ",rheight)

    ldiameter = diameter(root.left)
    #print("Left Diameter of ",root.left, " is ",ldiameter)
    rdiameter = diameter(root.right)
    #print("Right Diameter of ",root.right," is ",rdiameter)

    return max(lheight+rheight+1, max(ldiameter, rdiameter))

# Driver Code

# Test Case 1
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.left.right.left = Node(6)
r1.left.right.right = Node(7)
r1.right.right = Node(8)
r1.right.right.right = Node(9)
r1.right.right.right.left = Node(10)
r1.right.right.right.right = Node(11)
r1.right.right.right.left.right = Node(12)

print("Diameter of given tree is ",diameter(r1))

# Test Case 2
r2 = Node(1)
r2.left = Node(2)
r2.right = Node(3)
r2.left.left = Node(4)
r2.left.left.left = Node(5)
r2.left.left.right = Node(6)
r2.left.left.right.left = Node(7)
r2.left.left.right.left.right = Node(8)
r2.left.right = Node(9)
r2.left.right.right = Node(10)
r2.left.right.right.left = Node(11)
r2.left.right.right.right = Node(12)
r2.left.right.right.right.left = Node(13)

print("Diameter of given tree is ",diameter(r2))
