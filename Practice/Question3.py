#Minimum spanning tree, Applying something similar to Prim's
class Solution(object):
    def question3(self,G):
        if not G:return None
        val = []
        for node in G:
            val.append(self.dfsloop(node, G, [], []))
        return min(val)

    def dfsloop(self, n, G, visited, sum_):
        if n not in visited:
            visited.append(n)
            for tup in G[n]:
                if tup[0] in G:
                    if tup[0] not in visited: sum_.append(tup[1])
                    self.dfsloop(tup[0], G, visited, sum_)
        return sum(sum_)


obj=Solution()
G1={'A':[('B',2), ('C',3), ('D',1)],
   'B':[('A',2), ('D', 4)],
   'C':[('A',3), ('D',2)],
   'D':[('A',1), ('C',2), ('B',4)]
   }
G2={   'A':[('B',2), ('E',1), ('F',2), ('D',3), ('C',5)],
      'B':[('E',1), ('A',2), ('D',2), ('C',1)],
      'C':[('B',1), ('A',5)],
      'D':[('A',3), ('B',2), ('F',4)],
      'E':[('B',1), ('A',1)],
      'F':[('A',2), ('D',4)],
    }
G3={
   }
print(obj.question3(G1)) #6
print(obj.question3(G2)) #8
print(obj.question3(G3)) #None
