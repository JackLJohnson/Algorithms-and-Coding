'''
Construct a BST given a PreOrder and a Inorder traversal
 - Very similar to Binary search
 - Lets say the PreOrder and Inorder are lists
 - Leetcode problem - 105
 - https://discuss.leetcode.com/topic/21287/python-short-recursive-solution
'''
class Node(object):
    """docstring for Tree."""
    def __init__(self,data):
        super(Node, self).__init__()
        self.data = data
        self.left = None
        self.right = None

class Construct(object):
    """docstring for Construct."""
    def __init__(self):
        super(Construct, self).__init__()

    def buildTree(self, p,i):
        search={}
        for idx,val in enumerate(i):
            search[val]=idx
        return self.ConstructTree(search, p, i, 0,0,len(inorder))

    def ConstructTree(self, search, preorder, inorder, ps, ist, e):
        if ist==e:return None
        node = Node(preorder[ps])
        idx = search[preorder[ps]]
        node.left=self.ConstructTree(search, preorder, inorder, ps+1, ist, idx)
        node.right=self.ConstructTree(search, preorder, inorder, ps+1+idx-ist, idx+1,e)
        return node

    def buildTree2(self, preorder, inorder):
        if inorder:
            ind=inorder.index(preorder.pop(0))
            root=Node(inorder[ind])
            print(root.data)
            root.left = self.buildTree2(preorder, inorder[0:ind])
            root.right = self.buildTree2(preorder, inorder[ind+1:])
            return root

obj=Construct()
preorder=['A','B','D','F','G','E','C']
inorder= ['F','D','G','B','E','A','C']
res=obj.buildTree2(preorder,inorder)
print(res.data,res.left.data,res.right.data)
