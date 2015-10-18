"""
	A class that represent a Graph G. This graph was constructed
	for represent a dictionary of vertices and every vertex is
	a set.
"""
#!/usr/bin/env python3
from random import choice

class Graph(object):
	# Contructs a instance of the graph G
	def __init__(self, vertices={}, directed=False):
		self.vertices = vertices
		self.directed = directed

	# Add a vetex in the graph G
	def add_vertex(self, vertex):
		if vertex not in self.vertices:
			self.vertices[vertex] = set()

	# Remove a vertex in the graph G
	def remove_vertex(self, vertex):
		if vertex in self.vertices:
			for vert in self.vertices:
				if vertex in self.vertices[vert]:
					self.vertices[vert].remove(vertex)
			del self.vertices[vertex]

	# Connects (add a edge) between two given vertices.
	# If is a directed graph, if the function be called
	# like this:
	#		graph.connect(A, B)
	# The connection will be there:
	#		A -----> B
	def connect(self, vertex1, vertex2):
		if vertex1 in self.vertices and vertex2 in self.vertices:
			if self.directed == False:
				self.vertices[vertex1] = [vertex2]
				self.vertices[vertex2] = [vertex1]
			else:
				self.vertices[vertex1] = [vertex2]

	# Disconnects (remove the edges) between two given vertices
	# If is a directed graph, the remove is, for example,
	# two vertices A and B such that:
	#		A -----> B
	# this function should be called like this to remove the
	# connection:
	#		graph.disconnect(A, B) 
	def disconnect(self, vertex1, vertex2):
		if vertex1 in self.vertices and vertex2 in self.vertices:
			if self.directed == False:	
				self.vertices[vertex1].remove(vertex2)
				self.vertices[vertex2].remove(vertex1)
			else:
				self.vertices[vertex1].remove(vertex2)

	# Shows the order of the graph G
	def order(self):
		return len(self.vertices)

	# Get the set of the vertices of G
	def get_vertices(self):
		set_vertices = set(self.vertices.keys())
		return set_vertices

	# Return a random vertex
	def get_random_vertex(self):
		return choice(list(self.vertices.keys()))

	# Return a set with the vertex's adjacents
	def get_adjacents(self, vertex):
		set_adjacents = set()
		for vert in self.vertices:
			if vertex in self.vertices[vert]:
				set_adjacents.add(vert)
		return set_adjacents

	# Get the degree of emission of a given vertex
	def get_vertex_outdegree(self, vertex):
		return len(self.vertices[vertex])

	# Get the degree of reception of a given vertex
	def get_vertex_indegree(self, vertex):
		return len(self.get_adjacents(vertex))

	# Get the degree of a given vertex
	def get_degree(self, vertex):
		return len(self.get_adjacents(vertex))

	# Checks if the graph is a regular graph, so,
	# if every vertex has the same degree
	def is_regular(self):
		vertices = self.get_vertices()
		vertex = vertices.pop()
		base_degree = self.get_degree(vertex)
		length = len(vertices)
		while (length > 0):
			vertex = vertices.pop()
			degree = self.get_degree(vertex)
			if degree != base_degree:
				return False
			length = len(vertices)
		return True

	# Checks if the graph is a complete graph, so,
	# if every vertex is connect with all other 
	# vertices of the graph G
	def is_complete(self):
		set_vertices = self.get_vertices()
		for vertex in self.vertices:
			for element in set_vertices:
				if element not in self.vertices[vertex] and element is not vertex:
					return False
		return True

	def transitive_closure(self, vertex):
		adjacents = self.get_adjacents(vertex)
		list_adjacents = list(self.vertices[vertex].values())
		tc = adjacents
		while (len(adjacents) > 0):
			for element in adjacents:
				tc.add(self.get_adjacents(element))
			adjacents = set(list_adjacents.pop())
		return tc
