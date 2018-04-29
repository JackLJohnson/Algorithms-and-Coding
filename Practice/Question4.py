class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    #least common ancestor between two nodes on a binary search tree
    def question4(self, T, r, n1, n2):
        #Tree is a BST only, no need to check that
        return self.constructTree(T,r,n1,n2) #Construct and check LCA for the BST using the matrix

    def lca(self, root, n1, n2):
        if not root:return None
        if n1<root.val and n2<root.val:
            self.lca(root.left, n1, n2)
        if n1>root.val and n2>root.val:
            self.lca(root.right, n1, n2)

        return root.val


    def right_(self, node, data):
        newnode = Node(data)
        node.right=newnode
        return newnode

    def left_(self, node, data):
        newnode = Node(data)
        node.left=newnode
        return newnode

    def constructTree(self, T, r, n1, n2):
        nodes=[]
        root=Node(r)
        for idx, elem in enumerate(T[r]):
            if elem:
                if idx>r:nodes.append(self.right_(root, idx))
                else:nodes.append(self.left_(root, idx))
        #print(root.right.val, root.left.val)
        # Use BFS to construct the rest of the tree
        temp=nodes.pop(0)
        while temp:
            for idx, elem in enumerate(T[temp.val]):
                if elem:
                    if idx>temp.val:nodes.append(self.right_(temp, idx))
                    else:nodes.append(self.left_(temp, idx))
            if not nodes:
                break
            else:temp=nodes.pop(0)

        return self.lca(root, n1, n2)

obj=Solution()
print(obj.question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))
