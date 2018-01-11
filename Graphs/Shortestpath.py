'''
Using Dijkstra's Algorithm to find shortest path in a graph
For those of you seeking an additional challenge, try implementing the heap-based version. Note this requires a heap that supports deletions,
and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap

-helpers:
https://docs.python.org/3.6/library/heapq.html
https://dbader.org/blog/priority-queues-in-python

'''
import urllib as url1
import os
from os import path
import time
import re
import heapq

N=200
class shortestPath(object):
    """docstring for shortestPath."""
    def __init__(self):
        super(shortestPath, self).__init__()

    def gettingthefile(self, path):
        url = "https://d18ky98rnyall9.cloudfront.net/_dcf1d02570e57d23ab526b1e33ba6f12_dijkstraData.txt?Expires=1509062400&Signature=cuocj7kUiaCcb2I8Qij3TfxJ8B~0btP4ZPzAzSofwuAm9gyybx6S~sWD5UUluqwFnyAfJSXIouea2wQR3JrZZr0LgkspXAGaeLEnxWoSgGRKTQTNwhbKBL8kXHcoP-b91HCuUrEu4YAxQu82SFckIVgzqyteet8FNt70BCxLbFQ_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response = url1.urlopen(url)
        data = response.read()
        f1 = open(path, 'w')
        dijk = data.decode('utf-8')
        f1.write(dijk)
        f1.close()

    def processdata(self,path):
        f2 = open(path, 'r+')
        graph = {}
        for line in f2:
            temp = line.split("\t")
            for idx, val in enumerate(temp):
                if idx==0 and re.search(r'\d',val):
                    nodeval = int(val.strip())
                    graph[int(val.strip())] = []
                else:
                    if re.search(r'\d',val):
                        n=int(val.split(",")[0].strip())
                        d=int(val.split(",")[1].strip())
                        graph[nodeval].append(tuple((n,d)))
        return graph


    def dijkstras(self, g, source):
        nodes = list(g.keys()) #Priority Q , not require a set as all keys are unique
        d={}
        path = {}

        #initilize
        for node in nodes:
            if node!=source:
                d[node]=float('inf')
        d[source]=0 # Distance estimates from s(source) to x
        while nodes:
            min_node = None
            for node in nodes:
                if d[node]!=float('inf'):
                    if min_node is None:
                        min_node = node
                    elif d[node]<d[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node) #clear the stack , instad lets use a heap here
            current_weight = d[min_node]

            #Now use dijkstra's greedy criterion
            for val in g[min_node]:
                weight = current_weight + val[1]
                if d[val[0]] == float('inf') or weight < d[val[0]]:
                    d[val[0]] = weight
                    path[val[0]] = min_node

        return d,path

obj = shortestPath()
filename = "C://Public//Code//shortestPath//dijkstra.txt"
if os.path.isfile(filename):
    start = time.time()
    g = obj.processdata(filename)
    #print("1st two graph values", len(g[1]),len(g[2]))
    distance, path = obj.dijkstras(g,1)
    print(distance)
    print(path)
    print("time taken to process the file", time.time()-start)
else:
    obj.gettingthefile(filename)
