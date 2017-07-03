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
    - Getting the universal sink and the incident matrix and the matrix product representation
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

def issink(M, i, n):
    for j in range(1,n):
        if M[i][j] == 1:
            return False
        if (M[j][i] == 0 and i!=j):
            return False
    return True

def findsink(M,n):
    i=0
    j=0
    print(M)
    while (i<n and j<n):
        if M[i][j] == 0:
            j=j+1
        elif M[i][j] == 1:
            i=i+1
    if (i<n and issink(M,i,n)):
        print("The sink is at index: ", i)
    else:
        print("No universal Sink here")

def incidentmat(B):
    try:
        Bt = B.transpose()
        newval = np.dot(B, Bt)
        print("product \n", newval)
    except Exception as e:
        print(type(e))
        print(e.args)

def main():
    print("Addign the edges here \n")

    ch = input("Input a choice of Graph: 1-> random, 2-> directed connected Graph, 3 -> Undirected Graph \n")

    if int(ch) == 1:
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
    elif int(ch) == 2:
        g.addEdge(0,1,1)
        g.addEdge(0,3,4)
        g.addEdge(1,2,2)
        g.addEdge(2,0,3)
        g.addEdge(3,2,5)

    gdict = {}

    for v in g:
        for w in v.getConnections():
            if v.getId() in gdict.keys():
                if len(gdict[v.getId()])!=0:
                    gdict[v.getId()].append(w.getId())
                elif len(gdict[v.getId()]) == 0:
                    gdict[v.getId()] = [w.getId()]
            else:
                gdict[v.getId()] = [w.getId()]

    unique = []
    for key , val in gdict.items():
        print("key with", key, "has neighbors :", val)
        if key not in unique:
            unique.append(key)
        for x in val:
            if x not in unique:
                unique.append(x)

    print("unique items :", unique)

    # Adjacent Matrix representation
    '''
    A unique property of list of lists : https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
    '''
    adjmat = [[0]*len(unique) for x in range(len(unique))]

    for key, val in gdict.items():
        for item in val:
            adjmat[key][item] = 1

    print("The universal sink node: ",set(unique - gdict.keys()))

    # Matrix representation using numpy
    val = np.array(adjmat)
    print(val)
    #Find the universal Sink here
    findsink(val, len(unique))

    #Getting the incident matrix
    #TODO: Getting hardcoded here, Need to change this
    B = [[-1,0,1,-1,0],[1,-1,0,0,0],[0,1,-1,0,1],[0,0,0,1,-1]]
    Bnew = np.array(B)
    print(Bnew)
    incidentmat(Bnew)

## Adding the weights through user input
if __name__ == '__main__':
    main()
