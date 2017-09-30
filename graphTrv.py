'''
Using DFS to traverse a graph

Use dictionary to implement a graph
'''

#Forming a Random Connected Undirected graph to teaverse only
class Graph(object):
    """docstring for graph."""
    def __init__(self, graph_dict=None):
        super(Graph, self).__init__()
        if not graph_dict:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        '''
        assumes that edge is of type set, tuple or list
        between two edges there can be multiple edges

        if (a,b) are connected , a is the vertex1 and b is the vertex2
        '''
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = vertex2

    def __generate_edges(self):
        '''
        Static method generating the edges of the graph
        - Right now we only need all the unique edges and not repeated ones
        '''
        seen = set()
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if (neighbor,vertex) not in seen and (vertex, neighbor) not in seen:
                    edges.append((neighbor, vertex))
                    seen.add((neighbor,vertex))
        return edges

    def __str__(self):
        res = "vertices:"
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\n edges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def dfs(self,g,node,visited):
        if node not in visited:
            visited.append(node)
            for n in g[node]:
                self.dfs(g,n,visited)
        return visited

if __name__ == "__main__":
     g1 = {
        "a":["b","c"],
        "b":["a","c","f","e"],
        "c":["a","b","d","e"],
        "d":["c"],
        "e":["b","c","f"],
        "f":["b","e"]
     }

     g2 = {
        "a":["b","s"],
        "b":["a"],
        "c":["s","d","f","e"],
        "d":["c"],
        "e":["c","h"],
        "f":["c","g"],
        "g":["f","s","h"],
        "h":["e","g"],
        "s":["a","g","c"]
     }

     graph = Graph(g2)

     print("Vertices of the graph:")
     print(graph.vertices())

     print("Edges of the graph:")
     print(graph.edges())

     print("Depth first Search")
     print(graph.dfs(g2, "a", []))

    #  print("Add vertex:")
    #  graph.add_vertex("g") #Remember once you add the vertex make sure to connect it
     #
    #  print("Add an edge")
    #  graph.add_edge(("e","g"))
    #  graph.add_edge({"d","g"})
     #
    #  print("Vertices of the graph")
    #  print(graph.vertices())
     #
    #  print("Edges of the graph")
    #  print(graph.edges())
