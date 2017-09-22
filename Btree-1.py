'''
- Iterative Preorder traversal
<root><left subtree><right subtree>

- Iterative Inorder traversal
<left subtree> <root> <right subtree>

- Iterative PostOrder traversal
<left subtree> <right subtree> <root>
'''


class Node(object):
    """A Node Class"""
    def __init__(self, val):
        super(Node, self).__init__()
        self.arg = val
        self.left = None
        self.right = None
        self.parent = None

# Creating a Simple Binary Tree
'''
Currently this involves using Stack and not using function recurssion -> Better O(n)
'''
def iterativePreorder(root):

    #Base Case:
    if root is None:
        return

    #create a empty stack and push the root to it
    nodeStack = []
    nodeStack.append(root)

    #Pop all the items one by one.
    while(len(nodeStack) > 0):

        #Pop the top item from stack and print it
        node = nodeStack.pop()
        print node.arg

        #Push right and left children of the popped node to stack
        # we need to do this as this is LIFO Technique
        #TODO : Try this using a queue
        if node.right is not None:
            nodeStack.append(node.right)
        if node.left is not None:
            nodeStack.append(node.left)


def iterativeinorder(root):
    pass

# Inorder succesor of BST
def InorderSuccesor(node):
    print "chek1", node.arg
    res = []
    if node.right :
        res = lefttraversal(node.right, res)
        return res.pop()
    else:
        #return node.parent
        return None

def lefttraversal(node, res):
    res.append(node)
    if node.left :
        lefttraversal(node.left, res)
    return res

# Create Root
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.left.right.left = Node(11)
root.left.left.left = Node(6)
root.right.left = Node(17)
root.right.right = Node(25)
root.right.left.left = Node(16)
root.right.right.right = Node(27)

#iterativePreorder(root)
#nodetest = 10
print "final",InorderSuccesor(root.left).arg
