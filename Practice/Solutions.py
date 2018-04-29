'''
Question1
'''
from itertools import permutations
class Solution1(object):
    def question1(self,s,t):
        list_=permutations(t, len(t))
        for val in list_:
            if ''.join(val) in s:return True
        return False
obj=Solution1()

print(obj.question1("udacity","da"))  #True
print(obj.question1("udacity","man")) #False
print(obj.question1("udacity",""))    #True


'''
Question2
'''
class Solution2(object):
    def question2(self, a):
        #Longest palindrome - use dp to solve
        dp = [[0]*len(a) for i in range(len(a))]
        arev=a[::-1]
        len_res=0
        for i in range(len(a)):
            for l in range(len(a)):
                if arev[i]==a[l]:
                    count=0
                    for j in range(l,len(a)):
                        if i+count<len(a):
                            #print(a[j], arev[i+count], j, i+count)
                            if a[j]==arev[i+count]:dp[i][j] = dp[i][j-1]+1
                            else: dp[i][j]=dp[i][j-1]
                        count+=1
            len_res = max(max(dp[i]),len_res)
            #len_res=max(max(dp[i][:]),len_res))
        return len_res

obj=Solution2()

print(obj.question2("aa")) #2
print(obj.question2("madam")) #5
print(obj.question2("okalamadamask")) #7
print(obj.question2("abcdefg")) #1
print(obj.question2("")) #0


'''
Question3
'''
#Minimum spanning tree, Applying something similar to Prim's
class Solution3(object):
    def question3(self,G):
        if not G:return None
        val = []
        for node in G:
            val.append(self.dfsloop(node, G, [], []))
        return min(val)

    def dfsloop(self, n, G, visited, sum_):
        if n not in visited:
            visited.append(n)
            for tup in G[n]:
                if tup[0] in G:
                    if tup[0] not in visited: sum_.append(tup[1])
                    self.dfsloop(tup[0], G, visited, sum_)
        return sum(sum_)


obj=Solution3()
G1={'A':[('B',2), ('C',3), ('D',1)],
   'B':[('A',2), ('D', 4)],
   'C':[('A',3), ('D',2)],
   'D':[('A',1), ('C',2), ('B',4)]
   }
G2={   'A':[('B',2), ('E',1), ('F',2), ('D',3), ('C',5)],
      'B':[('E',1), ('A',2), ('D',2), ('C',1)],
      'C':[('B',1), ('A',5)],
      'D':[('A',3), ('B',2), ('F',4)],
      'E':[('B',1), ('A',1)],
      'F':[('A',2), ('D',4)],
    }
G3={
   }
print(obj.question3(G1)) #6
print(obj.question3(G2)) #8
print(obj.question3(G3)) #None


'''
Question4
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution4(object):
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

obj=Solution4()
print(obj.question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4))

'''
Question5
'''
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

# Find the element in a singly linked list that's m elements from the end
class Solution5(object):
    def question5(self, ll, m):
        res_=[]
        while ll:
            res_.append(ll.data)
            ll=ll.next
        return res_[-m]

# Test cases and Construct the linked List
ll=Node(2)
ll.next=Node(3)
ll.next.next=Node(4)
ll.next.next.next=Node(5)
ll.next.next.next.next=Node(6)

obj=Solution5()

print(obj.question5(ll,3)) #4
print(obj.question5(ll,2)) #5
print(obj.question5(ll,1)) #6
