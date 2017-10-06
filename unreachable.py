'''
You need to print a single integer denoting the number of nodes that are unreachable from the given head node
Reference :
-https://docs.python.org/2/library/stdtypes.html#set
-https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/

- Using DFS - Dpeth wise search
'''
import os
path = "./dfs_input.txt"
graph = {}
allnodes = set()
if os.path.exists(path):
    f = open(path,'rb+')
    for idx, line in enumerate(f):
        if idx == 0:
            N = int(line.split(" ")[0]) #Number of Nodes
            M = int(line.split(" ")[0]) #Number of Edges
        elif idx == M+1:
            head = str(line.strip())
            allnodes.add(head)
        else:
            a = str(line.split(" ")[0].strip())
            b = str(line.split(" ")[1].strip())
            allnodes.add(a)
            allnodes.add(b)
            if a not in graph:
                graph[a] = [b]
            else:
                graph[a].append(b)

print "The comlete Graph", graph

def dfs(node, g, visited):
    #Try dfs
    if node not in visited:
        visited.append(node)
        if node in g:
            for n in g[node]:
                dfs(n, g, visited)
    return visited


#print(list(allnodes))
#print(graph[head])
#print(allnodes - set(graph[head]))

res = dfs(head,graph,[])
print(len(res))
