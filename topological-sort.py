'''
- Form a DAG - Directed acyclic graph only
- using recurssive DFS but in the reverse way
- Use non recurssive DFS with distnce Also to solve this, where you pop out=
'''
#TODO to get the source node, there could be a case with multiple nodes, need to handle that
from collections import deque
import operator
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

    def tsort2(self,g):
        indegree = {node:0 for node in g}
        edges=[]
        for node in g:
            for k in g[node]:
                indegree[k]+=1
                edges.append((node, k))
        print("indegree", indegree)
        print("edges", edges)
        s = [key for key, val in indegree.items() if val==0][0]
        return self.dfs2(g, s, indegree, edges)

    def arragebyindegree(self, nodes, indegree):
        mydict = {val:indegree[val] for val in nodes}
        return [x[0] for x in sorted(mydict.items(), key=operator.itemgetter(1))]

    def dfs2(self, g, s, indegree, edges):
        l,stack,cnt,size = deque(),[s],0,len(g)
        while stack:
            item = stack.pop()
            l.append(item)
            for m in g[item]:
                indegree[m]-=1
                if indegree[m]==0:stack.append(m)
            cnt+=1
        return l if cnt==size else None

obj=TopologicalSort()
#dag={'a':['b','c'],'b':['d'],'c':['d','e'],'d':['f'],'e':['g'],'f':['g'],'g':[]}
dag={'a':['b','c'],'b':['d'],'c':['d','e'],'d':['f'],'e':['d','g'],'f':['g'],'g':[]}
print(obj.tsort2(dag))
