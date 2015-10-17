"""
	A class that represent a Graph G. This graph was constructed
	with represent a dictionary of vertices and every vertex is
	a dictionary.
"""
from random import choice

class Graph(object):
	# Contructs a intance of the graph G
	def __init__(self, vertices={}, directed=False, valued=False):
		self.vertices = vertices
		self.directed = directed
		self.valued = valued

	# Add a vetex in the graph G
	def add_vertex(self, vertex):
		if vertex not in self.vertices:
			self.vertices[vertex] = {}

	# Remove a vertex in the graph G
	def remove_vertex(self, vertex):
		if vertex in self.vertices:
			del self.vertices[vertex]
			for v in self.vertices:
				if vertex in v:
					del v[vertex]

	# Connects (add a edge) between two given vertices
	def connect(self, vertex1, vertex2):
		if vertex1 in self.vertices and vertex2 in self.vertices:
			self.vertices[vertex1] = vertex2
			self.vertices[vertex2] = vertex1

	# Disconnects (remove the edges) between two given vertices 
	def disconnect(self, vertex1, vertex2):
		if vertex1 in self.vertices and vertex2 in self.vertices:
			del self.vertices[vertex1][vertex2]
			del self.vertices[vertex2][vertex1]

	# Shows the order of the graph G
	def order(self):
		return len(self.vertices)

	# Get the set of the vertices of G
	def get_vertices(self):
		set_vertices = set()
		set_vertices.add(self.vertices)
		return set_vertices

	# Return a random vertex
	def get_random_vertex(self):
		return choice(self.vertices.keys())

	# Return a set with the vertex's adjacents
	def get_adjacents(self, vertex):
		set_adjacents = set()
		set_adjacents.add(self.vertices[vertex])
		for v in self.vertices:
			if vertex in v:
				set_adjacents.add(v)
		return set_adjacents

	# Get the degree of emission of a given vertex
	def get_vertex_outdegree(self, vertex):
		return len(self.vertices[vertex])

	# Get the degree of reception of a given vertex
	def get_vertex_indegree(self, vertex):
		count = 0
		for v in self.vertices:
			if vertex in v:
				count = count + 1
		return count

	# Get the degree of a given vertex
	def get_degree(self, vertex):
		return len(self.get_adjacents(vertex))
