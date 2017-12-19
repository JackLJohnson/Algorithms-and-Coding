'''
- Form a DAG - Directed acyclic graph only
- using recurssive DFS but in the reverse way
- Use non recurssive DFS with distnce Also to solve this, where you pop out
'''
from collections import deque
class TopologicalSort(object):
    """docstring for TopologicalSort."""
    def __init__(self):
        super(TopologicalSort, self).__init__()

    def tsort(self,g):
        visited=set()
        reversePostOrder=[]
        for node in g: #This just executes once for this case
            if node not in visited:
                self.dfs(g,node,visited,reversePostOrder)
        return reversePostOrder[::-1]

    def dfs(self,g,s,visited,reversePostOrder):
        #print("start",s,visited)
        if s not in visited:
            visited.add(s)
            if s in g:
                for n in g[s]:
                    self.dfs(g,n,visited,reversePostOrder)
            reversePostOrder.append(s)
            #print(reversePostOrder)

obj=TopologicalSort()
dag={'a':['b','c'],'b':['d'],'c':['d','e'],'d':['f'],'e':['g'],'f':['g'],'g':[]}
print(obj.tsort(dag))
