#!/usr/bin/env python3
#	A class that represent a Graph G. This graph was constructed
#	for represent a dictionary of vertices and every vertex is
#	a set. The structure of the graph G it is presented as follows:
#			G = {
#				v1:set{v2, vn},
#				v2:set{v1, vn},
#				v3:set{},
#				vn:set{v1, v2}
#			}
#	Where G is a dictionary representing the graph, v1, v2 and 
#	vn where sets representing the vertices and the elements in
#	each set are the adjancets vertices of the respective vertex.
#
# :author: Caique Marques
# :license: Gnu General Public License version 3
#
from random import choice

class Graph(object):
	#########################
	#     Basic Actions	#
	#########################
	# Basic actions for a undirected graph or directed graph

	def __init__(self, vertices={}, directed=False):
		"""
		Constructs a instance of the graph G

		:param vertices: The vertices of the graph,
			each vertex is a set.
		:param directed: If is a graph directed or not,
			not is, by defatult.
		"""
		self.vertices = vertices
		self.directed = directed

	def add_vertex(self, vertex):
		"""
		Add a vetex in the graph G

		:param vertex: The vertex that will
			be added in the graph
		"""
		if vertex not in self.vertices:
			self.vertices[vertex] = set()

	def remove_vertex(self, vertex):
		"""
		Remove a vertex in the graph G

		:param vertex: The vertex that will
			be removed in the graph
		"""
		if vertex in self.vertices:
			for vert in self.vertices:
				if vertex in self.vertices[vert]:
					self.vertices[vert].remove(vertex)
			del self.vertices[vertex]

	def connect(self, vertex1, vertex2):
		"""
		Connects (add a edge) between two given vertices.
		If is a directed graph, if the function be called
		like this:
			graph.connect(A, B)
		The connection will be there:
			A -----> B

		:param vertex1: A vertex that will be connected with
			other vertex, so, the vertex2
		:param vertex2: A vertex that will be connected with
			other vertex, so, the vertex1
		"""
		if vertex1 in self.vertices and vertex2 in self.vertices:
			if self.directed == False:
				self.vertices[vertex1] = [vertex2]
				self.vertices[vertex2] = [vertex1]
			else:
				self.vertices[vertex1] = [vertex2]
 
	def disconnect(self, vertex1, vertex2):
		"""
		Disconnects (remove the edges) between two given vertices
		If is a directed graph, the remove is, for example,
		two vertices A and B such that:
			A -----> B
		this function should be called like this to remove the
		connection:
			graph.disconnect(A, B)

		:param vertex1: A vertex that will be disconnected with
			other vertex, so, the vertex2
		:param vertex2: A vertex that will be disconnected with
			other vertex, so, the vertex1
		"""
		if vertex1 in self.vertices and vertex2 in self.vertices:
			if self.directed == False:	
				self.vertices[vertex1].remove(vertex2)
				self.vertices[vertex2].remove(vertex1)
			else:
				self.vertices[vertex1].remove(vertex2)

	def order(self):
		"""
		Shows the order of the graph G. Order of a graph
		is the number of vertices of this graph.
		"""
		return len(self.vertices)

	def get_vertices(self):
		"""
		Get the set of the vertices of G
		"""
		set_vertices = set(self.vertices.keys())
		return set_vertices

	def get_random_vertex(self):
		"""
		Return a random vertex
		"""
		return choice(list(self.vertices.keys()))

	def get_adjacents(self, vertex):
		"""
		Return a set with the vertex's adjacents

		:param vertex: The vertex that their adjacents
			will be added in the set.
		"""
		set_adjacents = set()
		for vert in self.vertices:
			if vertex in self.vertices[vert]:
				set_adjacents.add(vert)
		return set_adjacents

	def get_vertex_outdegree(self, vertex):
		"""
		Get the degree of emission of a given vertex

		:param vertex: The vertex that the degree of
			emission will ve returned
		"""
		return len(self.vertices[vertex])

	def get_vertex_indegree(self, vertex):
		"""
		Get the degree of reception of a given vertex

		:param vertex: The vertex that the degree of
			reception will ve returned
		"""
		return len(self.get_adjacents(vertex))

	def get_degree(self, vertex):
		"""
		Get the degree of a given vertex. Degree
		of a vertex is the number of this adjacents
		vertices

		:param vetex: The vertex that the degree
			will be returned
		"""
		return len(self.get_adjacents(vertex))

	#########################
	#  Derivative Actions	#
	#########################
	# Derivative actions for a undirected graph

	def is_regular(self):
		"""
		Checks if the graph is a regular graph, so,
		if every vertex of G has the same degree
		"""
		base_degree = self.get_degree(self.get_random_vertex())
		for v in self.vertices:
			if self.get_degree(v) is not base_degree:
				return False
		return True

	def is_complete(self):
		"""
		Checks if the graph is a complete graph, so,
		if every vertex is connect with all other 
		vertices of the graph G
		"""
		n = self.order() - 1
		for v in self.vertices:
			if self.get_degree(v) is not n:
				return False
		return True

	def transitive_closure(self, vertex, visited=set()):
		"""
		Returns a set content every vertices of G that 
		are transitively reachable starting in "vertex"

		:param vertex: Starting vertex to see every 
			vertex reachable from it.
		:param visited: Set with the visited vertices.
		"""
		visited.add(vertex)
		for adjacent in self.get_adjacents(vertex):
			if adjacent not in visited:
				self.transitive_closure(adjacent, visited)
		return visited

	def is_connected(self):
		"""
		Checks if there is at least one path between 
		each pair of vertices of G
		"""
		return set(self.vertices.keys()) == self.transitive_closure(self.get_random_vertex())

	def has_cycle(self, vertex, actual_v, previous_v, visited=set()):
		"""
		Checks if the graph G has a cycle

		:param vetex: Initial vertex.
		:param actual_v: Actual vertice to compare with
			their adjacents vertices.
		:param previous_v: Previous vertex of actual_v.
		:param visited: Set with all vertices visited.
		"""
		if actual_v in visited:
			return actual_v is vertex
		visited.add(actual_v)
		for adjacent in self.get_adjacents(vertex):
			if adjacent != previous_v:
				if self.has_cycle(vertex, adjacent, actual_v, visited):
					return True
		visited.remove(actual_v)
		return False

	def is_tree(self):
		"""
		Checks if the graph G is a tree, in other words,
		if G not has cycle and if G is a connected graph
		"""
		vertex = self.get_random_vertex()
		return self.is_connected() and not(self.has_cycle(vertex, vertex, None, set()))
