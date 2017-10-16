'''
Implementing the Kosaraju's Algorithm to find SCCs in a graph
'''
import urllib.request as url1
import os
from os import path
from collections import defaultdict
import sys , time
#import resource

#Increase recursion limit and stack size
sys.setrecursionlimit(2 ** 20)
#maxlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
#resource.setrlimit(resource.RLIMIT_STACK,(maxlimit,maxlimit))

GRAY=0 #visited
BLACK=1 #finished
#N=875714 #number of Nodes
N=9

class findScc(object):
    """docstring for findScc."""
    def __init__(self, path):
        super(findScc, self).__init__()
        self.path = path


    def gettingthefile(self):
        url = "https://d18ky98rnyall9.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1508198400&Signature=lJZDGX5qNV0vY3d40X1dgP~~-iHhFSEYKVkbBakwAzzwPM5kASDGI32VqtdD~Tx1GQMAF21nV15sSjzqZ6ePubmy8LDZgl9BfeKi02y8e7NAJ-Zc-aY-G6yquD9hiu0b9y~YtJtxA1glA87vYf9U8vgb2ThllJfOIScU5ImOXrk_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response = url1.urlopen(url)
        data=response.read()
        #wd = 'C:/Public/Code/scc/'
        #filename = path.join(wd,'scc.txt')
        filename = self.path
        file = open(filename, "w")
        scc = data.decode('utf-8')
        file.write(scc)
        file.close

    def processdata(self, path):
        file1 = open(path, "r+")
        graph, graphrev = defaultdict(list),defaultdict(list)
        for line in file1:
            graph[int(line.split(" ")[0].strip())].append(int(line.split(" ")[1].strip()))
            graphrev[int(line.split(" ")[1].strip())].append(int(line.split(" ")[0].strip()))
            #graph[line.split(" ")[0].strip()].add(line.split(" ")[1].strip())
        return graph, graphrev


    def Kosaraju(self, g, grev):
        global leader, finished
        leader = {}
        finished = {}
        self.DFSLoop(grev) #first pass
        # Reorder based on finishing times
        G_reord = {}
        g_val = list(g.values())
        print(g_val)
        for i in range(1, N+1):
            temp = g_val[i-1]
            G_reord[finished[i]] = [finished[x] for x in temp]
        # Run second DFS on the reordered G
        self.DFSLoop(G_reord)
        return leader


    def DFSLoop(self,g):
        global t, s, explored
        t=0 #visited so far
        s=0 # Current source
        explored = {} #initilize all nodes as unexplored
        for i in range(1, N+1):
            explored[i] = 0
        for i in range(N,0,-1):
            if explored[i]==0:
                s=i
                self.dfs(g,i)
        return


    def dfs1(self, g, start):
        '''
        For loop might not be efficient, use a stack instead
        '''
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(g[vertex]-visited)
        return visited

    def dfs(self, g, i):
        '''
        For loop: recurssion
        '''
        global t
        explored[i]=1
        leader[i] =s
        for j in g[i]:
            if explored[j]==0:
                self.dfs(g,j)
        t=t+1
        finished[i]=t

    def topcommon(self, x,y):
        from collections import Counter
        c = Counter(x)
        result = []
        for number , count in c.most_common(y):
            result.append(count)
        return result


filename = "C:/Public/Code/scc/scc1.txt"
obj = findScc(filename)
if os.path.isfile(filename):
    start = time.time()
    g,grev = obj.processdata(filename)
    print("time taken for getting graph", time.time()-start,"seconds")

    start = time.time()
    leader = obj.Kosaraju(g,grev)
    print("time taken for Implementing Kosaraju's Algorithm", time.time()-start,"seconds")

    print("Size of top 5 strongly connected components:")
    print(obj.topcommon(list(leader.values()), 5))

else:
    obj.gettingthefile(filename)
