'''
@author: Sandeep Anand
- This Code is for analysis of Trees as the data structure of choice
'''

# A Python class that reprsents the individual node
'''
A Tree contains the following parts.

Binary tree is a data structure in which each node has "at most", only two children

- data
- Pointer to the left child
- Pointer to the right child
'''
class Node(object):
    """docstring for Node."""
    def __init__(self, key):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return str(self.val)

# Creating a simple tree with 7 nodes/vertices
#create root
root=Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

# Traversing the tree to print out everything
def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level=next_level

traverse(root)
