'''
DFS and BFS
- DFS - always use stacks
- BFS - always use queues
'''
class graphSearch(object):
	def __init__(self, g):
		self.graph = g
		self.visited=[]

	def dfs(self):
		def dfs_visit(vertex, g):
			if vertex not in self.visited:
				self.visited.append(vertex)
				for node in g[vertex]:
					dfs_visit(node, g)
			return self.visited
			
		for v in self.graph:
			dfs_visit(v, self.graph)
		print(self.visited)

		





	def bfs(self):
		pass

if __name__ == "__main__":
	g1 = {"a":["a","b"],"b":["e"],"c":["e","f"],"d":["b"],"e":["d"],"f":["f"]}
	obj = graphSearch(g1)
	obj.dfs()

