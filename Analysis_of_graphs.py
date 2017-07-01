'''
@author: Sandeep Anand

- Making a graph class
- Use of https://networkx.github.io/documentation/networkx-1.10/reference/classes.multigraph.html
- Implementation
    - Each vertex used a dictionary(connectedto) of key = nbr(vrtx) and value = weight
    - addneighbor() adds the neighbor with a weight to this vertex
    - getConnections() returns all of the vertices in the adjacency list
    - getId() returns the id
    - getWeight() returns the weight of the edge from this vertex to the vertex passed as the parameter
'''

import numpy as np
import random

class Vertex(object):
    """docstring for ."""
    def __init__(self, key):
        super(Vertex, self).__init__()
        self.id = key
        self.connectedto = {}

    def addneighbor(self, nbr, weight=0):
        self.connectedto[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected To: ' + str([x.id for x in self.connectedto])

    def getConnections(self):
        return self.connectedto.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedto[nbr]
'''
Graph class maps the vertex names to the vertex objects.
Also this has member functions for adding vertices to the graph
and connecting one vertex to the other
 - getVertices() - returns the names of all the vertices in the graph
 - __iter__ method to make it easy to iterate over all the vertex objects in a particular graph

'''
class Graph(object):
    """docstring for Graph."""
    def __init__(self):
        super(Graph, self).__init__()
        self.vertlist = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertlist[key] = newVertex

    def getVertex(self, n):
        if n in self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertlist

    def addEdge(self, f, t, cost=0):
        if f not in self.vertlist:
            nv = self.addVertex(f)
        if t not in self.vertlist:
            nv = self.addVertex(t)
        self.vertlist[f].addneighbor(self.vertlist[t], cost)

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())

g = Graph()
for i in range(8):
    g.addVertex(i)

print("Printing out the nodes here", g.vertlist.keys())

def main():
    print("Addign the edges here \n")
    g.addEdge(0,1,5)
    g.addEdge(0,6,6)
    g.addEdge(0,5,2)
    g.addEdge(1,6,6)
    g.addEdge(1,2,3)
    g.addEdge(2,3,5)
    g.addEdge(3,7,2)
    g.addEdge(4,3,8)
    g.addEdge(5,6,2)
    g.addEdge(5,4,6)
    g.addEdge(7,6,2)
    g.addEdge(7,8,4)
    g.addEdge(8,2,9)

    for v in g:
        for w in v.getConnections():
            print("(%s, %s)" % (v.getId(), w.getId()))
## Adding the weights through user input
if __name__ == '__main__':
    main()
