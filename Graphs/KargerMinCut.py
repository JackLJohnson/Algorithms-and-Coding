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
                edges.add([t[0],t[1]])
                edges.add([t[1],t[0]])
        return graph,edges

    def getmincut(self, edges, nodelist):
        while len(nodelist)>2:
            idx=randint(0,(len(edges)-1)) #randomly get an edge to remove
            snode,tnode=edges[idx][0],edges[idx][1]
            nodelist.remove(snode)
            #print(snode, tnode, nodelist, edges)
            for e in edges:
                if e[0]==snode or e[1]==snode:
                    if e[0]==snode:e[0]=tnode
                    else:e[1]=tnode
            for e in edges:
                if e[0]==e[1]: edges.remove(e)
        print(edges)
        return (len(edges))

    # def updategraph(self, edges, nodelist):
    #     newg,vertices={},g.keys()
    #     for v in g[n]:
    #         if v not in g:continue
    #         k=v+n
    #         newg[k]=[]
    #         #print(g[v],v,k)
    #         for j in g[v]:
    #             if j not in vertices:continue
    #             if j!=n and j not in g[n]:newg[k].append(j)
    #             if j!=n and j in g[n]:
    #                 newg[k].append(j)
    #                 newg[k].append(j+n)
    #     for k,v in g.items():
    #         if k not in g[n] and k!=n:
    #             newg[k]=v
    #     return newg

if __name__ == "__main__":
    #file_="C:/Public/Code/testcases/KargetMincut.txt"
    file_="C:/Public/Code/testcases/kcuttc1.txt"
    obj=mincut()
    if os.path.isfile(file_):
        g,e=obj.processdata(file_)
        nodes=list(g.keys())
        min_=obj.getmincut(deepcopy(e),deepcopy(nodes))
        print(min_)
        for i in range(10):
            val=obj.getmincut(deepcopy(e),deepcopy(nodes))
            if val<min_:
                min_=val
        print(min_)
    else:
        obj.gettingthefile(file_)
