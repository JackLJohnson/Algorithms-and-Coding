'''
@Bellman-Ford
- Finding shortest path in case of negative weights
- check if there is a negative path present
- Maximum complexilty O(VE)
- eg: https://www.youtube.com/channel/UC6-g6xhqyX14ENhZBC2fznw/videos
'''
class bellmanford(object):
    """docstring for bellmanford."""
    def __init__(self):
        super(bellmanford, self).__init__()
    def traverse(self,g,s,t):
        nodes = g.keys()
        d={}
        pi={}

        for node in g:
            if node==s:d[node]=0
            else: d[node]=float('inf')
            pi[node]=None
        edges={}
        for node, edge in g.items():
            for val in edge:
                edges[(node,val[0])] = val[1]
        for node in g:
            for key,val in edges.items():
                #relaxation of (u,v) , v is the node , complexilty is  O(VE)
                tempdist = d[key[0]]+val
                if tempdist<d[key[1]]:
                    d[key[1]]=tempdist
                    pi[key[1]]=key[0]
        for key, val in edges.items():
            if d[key[0]]+val < d[key[1]]:
                print("there is a negative edge")
        return d,pi

g = {'s':[('a',5),('c',-2)], 'a':[('b',1)], 'c':[('a',2),('d',3)], 'b':[('c',2),('d',7),('t',3)],'t':[],'d':[('t',10)]}
source = 's'
target = 't'
obj = bellmanford()
distances , previous = obj.traverse(g, source, target)
print(distances,previous)
