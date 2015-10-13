"""
	A class that represent a Graph G. This graph was constructed
	with represent a dictionary of vertices and every vertex is
	a set.
"""
class Graph(object):
	# Contructs a intance of the graph G
	def __init__(self, vertices={}, directed=False, valued=False):
		self.vertices = vertices
		self.directed = directed
		self.valued = valued

	# Add a vetex in the graph G
	def add_vertex(self, vertex):
		if vertex not in self.vertices:
			self.vertices[vertex] = set()

	# Connects (add a edge) between two given vertices
	def connect(self, vertex1, vertex2):
		self.vertices[vertex1].add(vertex2)
		self.vertices[vertex2].add(vertex1)

	# Disconnects (remove the edges) between two given vertices 
	def disconnect(self, vertex1, vertex2):
		self.vertices[vertex1].remove(vertex2)
		self.vertices[vertex2].remove(vertex1)

	# Shows the order of the graph G
	def order(self):
		return len(self.vertices)

	# Get the set of the vertices of G
	def get_vertices(self):
		set_vertices = set()
		set_vertices.add(self.vertices)
		return set_vertices

	def get_adjacents(self, vertex):
		if vertex in self.vertices:
			set_adjacents = set()
			set_adjacents.add(self.vertices[vertex])
			for v in self.vertices:
				if v == vertex:
					set_adjacents.add(v)
			return set_adjacents

	# Get the degree of emission of a given vertex
	def get_outdegree(self, vetex):
		if vetex in self.vertices:
			return len(self.vertices[vertex])

	# Get the degree of reception of a given vertex
	def get_indegree(self, vertex):
		count = 0
		if vertex in self.vertices:
			for v in self.vertices:
				if vertex == v:
					count = count + 1
			return count

	# Get the degree of a given vertex
	def get_degree(self, vetex):
		return get_outdegree(vertex) + get_indegree(vertex)
