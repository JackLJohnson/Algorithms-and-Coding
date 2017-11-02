'''
Delete From a Binary Search tree
'''
class Node(object):
    """docstring for DeleteNodebst."""
    def __init__(self, val):
        super(Node, self).__init__()
        self.val = val
        self.left = None
        self.right = None

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if node.val<root.val:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)

def preOrderT(root):
    if root:
        print(root.val)
        preOrderT(root.left)
        preOrderT(root.right)

def InOrderT(root):
    if root:
        preOrderT(root.left)
        print(root.val)
        preOrderT(root.right)

def deleteNode(root, node):
    pass

#Forming the Binary Search Tree using the insert operation
r=Node(50)
insertNode(r,Node(30))
insertNode(r,Node(70))
insertNode(r,Node(20))
insertNode(r,Node(40))
insertNode(r,Node(60))
insertNode(r,Node(80))

#Traversing to check the tree
InOrderT(r)
