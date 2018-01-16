'''
Karger Min Cut Problem
'''
import urllib.request as url1
import os
import os as path
import sys
from random import randint
from copy import deepcopy
N=8 # Number of vertices

class mincut(object):
    def __init__(self):
        super(mincut, self).__init__()

    def gettingthefile(self, path):
        url="https://d18ky98rnyall9.cloudfront.net/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt?Expires=1516147200&Signature=OfldiZQ3RJCIpUi48B55IQmDWy-UWT0T4LcGlIhhXhNKAlJkkaTJKCo95wEpGgZeOLCgp~YcmazwDm2ofmmqEvwJXDDD5OB8binI~Ge1I4Qzay6zwJ0VP8PfPy-6yXIe5RJt4OeWCuOOb0kHRyI8viJrh2yuZembF-MXiA5jp2Q_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
        response=url1.urlopen(url)
        data=response.read()
        filename=path
        file_=open(filename, 'w')
        doc=data.decode('utf-8')
        file_.write(doc)
        file_.close

    def processdata(self, path):
        file_=open(path, "r+")
        graph,edges={},[]
        for line in file_:
            t=line.split()
            if len(t)!=0:
                graph[t[0]]=t[1:]
        for k, v in graph.items():
            for t in v:
                edges.append([k,t])
        return graph

    def get_random_edge(self):
        global g
        v1=list(g.keys())[randint(0,len(g)-1)]
        v2=g[v1][randint(0,len(g[v1])-1)]
        return (v1,v2)

    def getmincut(self):
        global g
        #print(g)
        while len(g)>2:
            edge=self.get_random_edge() #randomly get an edge to remove
            snode,tnode=edge[0],edge[1]
            #print(edge)
            # Replace tnode with snode, remove tnode from graph
            g[snode].extend(g[tnode])
            del g[tnode]

            # Replace all occurrence of tnode with snode
            for k, v in g.items():
                g[k] = [snode if temp==tnode else temp for temp in v]

            # #Remove all self loops, snode to itself
            g[snode]=[x for x in g[snode] if x!=snode]

            #print(g)

if __name__ == "__main__":
    #file_="C:/Public/Code/testcases/KargetMincut.txt"
    file_="C:/Public/Code/testcases/kcuttc3.txt"
    obj=mincut()
    minlist=[]
    if os.path.isfile(file_):
        g=obj.processdata(file_)
        for i in range(100):
            min_=obj.getmincut()
            minlist.append(len( g[list(g.keys())[0]]  ))
        print(min(minlist))
    else:
        obj.gettingthefile(file_)
