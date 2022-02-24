import sys

class Graph():
	def __init__(self, vertex):
		self.V = vertex
		self.graph = [[0 for column in range(vertex)] for row in range(vertex)]
        
	def dijkstra(self, source):
		dist = [sys.maxsize] * self.V
		dist[source] = 0
		tree = [False] * self.V
		for i in range(self.V):
			c = self.d(dist, tree)
			tree[c] = True
			for r in range(self.V):
				if self.graph[c][r] > 0 and	tree[r] == False and dist[r] > dist[c] + self.graph[c][r]:
					dist[r] = self.graph[c][r]+dist[c] 
		for i in range(self.V):
			print(i, "  ", dist[i])

	def d(self, dist, tree):
		min = sys.maxsize
		for i in range(self.V):
			if dist[i] < min and tree[i] == False:
				min = dist[i]
				pos = i
		return pos


nodes = Graph(7)
nodes.graph = graph = [[0, 2, 6, 0, 0, 0, 0], 
        [2, 0, 0, 5, 0, 0, 0], 
        [6, 6, 0, 8, 0, 0, 0], 
        [0, 0, 8, 0, 10, 15, 0], 
        [0, 0, 0, 10, 0, 6, 2], 
        [0, 0, 0, 15, 6, 0, 6], 
        [0, 0, 0, 0, 2, 6, 0],
        ];

print("output \nNode Distance from 0 ")
nodes.dijkstra(0)