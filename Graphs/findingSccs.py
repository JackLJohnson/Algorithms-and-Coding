'''
Implementing the Kosaraju's Algorithm to find SCCs in a graph
'''
#import urllib.request as url1
import urllib as url1
import os
from os import path
from collections import defaultdict
import sys , time
from collections import deque
#!/usr/bin/env python3.6

import resource
#Increase recursion limit and stack size

GRAY=0 #visited
BLACK=1 #finished
N=875714 #number of Nodes
#N=9

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
        graph, graphrev = {}, {}
        for i in range(1, N+1):graph[i], graphrev[i] = [], []
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
        #print("After first pass", finished)
        # Reorder based on finishing times
        G_reord = {}
        g_val = list(g.values())
        #print(g_val[0:3])
        sources = len(g_val) # This shows that all the nodes are not source nodes, but still it has to match
        #print(sources, len(finished))
        for i in range(1, sources+1):
            #print("chkerr", i)
            temp = g_val[i-1]
            G_reord[finished[i]] = [finished[x] for x in temp]
        #print("reordered", G_reord)
        # Run second DFS on the reordered G
        self.DFSLoop(G_reord)
        #print(leader)
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
                #print("chk dfs entry",i)
                #self.dfs(g,i)
                self.dfsalt(g,i)
                #print("return", finished)
        return

    def dfs(self, g, i):
        '''
        For loop: recurssion
        '''
        global t
        explored[i]=1
        leader[i] =s #Think of this only for 2nd Pass
        #print("chk", leader, explored,' ', t, " ", finished)
        for j in g[i]:
            if explored[j]==0:
                self.dfs(g,j)
        t+=1
        finished[i]=t
        return

    def dfsalt(self, g, i):
        '''
        For loop might not be efficient, use a stack instead
        '''
        global t
        #explored[i]=1
        #leader[i]=s # Think of this for 2nd pass only
        visited, stack, order = set(), [i], deque()
        while stack:
            vertex = stack.pop()
            #print("chk1", vertex)
            if vertex not in visited and explored[vertex]==0:
                visited.add(vertex)
                explored[vertex]=1
                leader[vertex]=s
                order.appendleft(vertex)
                #print("chk2",set(g[vertex])-visited, order)
                if len(set(g[vertex])-visited) ==0:
                    t+=1
                    finished[vertex]=t
                    order.popleft()
                stack.extend(set(g[vertex])-visited)
        #get everything left in the deque popleft and fill up finished
        while order:
            t+=1
            finished[order.popleft()]=t
        #print("end", order, finished)
        return

    def topcommon(self, x,y):
        from collections import Counter
        c = Counter(x)
        result = []
        for number , count in c.most_common(y):
            result.append(count)
        return result

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

filename = "C:/Public/Code/scc/scc.txt"
obj = findScc(filename)
if os.path.isfile(filename):
    start = time.time()
    g,grev = obj.processdata(filename)
    print("time taken for getting graph", time.time()-start,"seconds")

    start = time.time()
    leader = obj.Kosaraju(g,grev)
    print("time taken for Implementing Kosaraju's Algorithm", time.time()-start,"seconds")

    print("Size of top 5 strongly connected components:")
    print(obj.topcommon(list(leader.values()), 10))

else:
    obj.gettingthefile(filename)
