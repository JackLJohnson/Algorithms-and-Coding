'''
insert and Search from a BST
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
        InOrderT(root.left)
        print(root.val)
        InOrderT(root.right)

'''
1. No Child
2. One Child
3. Two Children
'''
def deleteNode(root, delelteval):
    if not root: return root
    if root.val>delelteval:
        root.left = deleteNode(root.left, delelteval)
    elif root.val<delelteval:
        root.right = deleteNode(root.right, delelteval)
    else:
        #Found the node to delete
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            root.val = getmin(root.right) #replace the delnode value with the minimum value (InOrder Succesor) of the right subtree
            root.right = deleteNode(root.right, root.val)
    return root

def getmin(root):
    minimum = 0
    if root:
        minimum = root.val
        getmin(root.left)
    return minimum

#Forming the Binary Search Tree using the insert operation
r=Node(50)
insertNode(r,Node(30))
insertNode(r,Node(70))
insertNode(r,Node(20))
insertNode(r,Node(40))
insertNode(r,Node(60))
insertNode(r,Node(80))

#Traversing to check the tree
print("After insertion")
InOrderT(r)

deleteNode(r, 30)
print("After Deletion")
#Traversing to check the tree
InOrderT(r)
