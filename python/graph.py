#!/usr/bin/env python3
#   A class that represent a Graph G. This graph was constructed
#   for represent a dictionary of vertices and each vertex is
#   a dict too. The structure of a undirected graph G it is presented
#   as follows:
#           G = {
#               v1:dict{v2:None, vn:None},
#               v2:dict{v1:None, vn:None},
#               v3:dict{},
#               vn:dict{v1:None, v2:None}
#           }
#   Where G is a dictionary representing the graph, v1, v2, v3 and 
#   vn where dictionaries representing the vertices and the elements in
#   each dict are the adjancets vertices of the respective vertex. The 
#   value "None" represents a value or a weigth for an edge, for a
#   valued graph, the values can be a integer, a real number, etc.. 
#
# :author: Caique Marques
# :license: Gnu General Public License version 3
#
from random import choice

class Graph(object):
    #######################
    #    Basic Actions    #
    #######################
    # Basic actions for a undirected graph, directed graph
    # valued directed graph or valued undirected graph.

    def __init__(self, vertices={}, directed=False, valued=False):
        """
        Constructs a instance of the graph G

        :param vertices: The vertices of the graph,
            each vertex is a set.
        :param directed: If is a graph directed or not,
            it is not, by default.
        :param valued: If is a graph valued or not,
            it is not, by default.
        """
        self.vertices = vertices
        self.directed = directed
        self.valued = valued

    def add_vertex(self, vertex):
        """
        Add a vetex in the graph G

        :param vertex: The vertex that will
            be added in the graph
        """
        if vertex not in self.vertices:
                self.vertices[vertex] = {}

    def remove_vertex(self, vertex):
        """
        Remove a vertex in the graph G

        :param vertex: The vertex that will
            be removed in the graph
        """
        if vertex in self.vertices:
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    del self.vertices[v][vertex]
            del self.vertices[vertex]

    def connect(self, vertex1, vertex2, value=None):
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
        :param value: The value of edge that connects vertex1
            with vertex2, None by default.
        """
        if vertex1 and vertex2 in self.vertices:
            if not self.directed:
                self.vertices[vertex1][vertex2] = value
                self.vertices[vertex2][vertex1] = value
            else:
                self.vertices[vertex1][vertex2] = value

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
        if vertex1 and vertex2 in self.vertices:
            if not self.directed:
                del self.vertices[vertex1][vertex2]
                del self.vertices[vertex2][vertex1]
            else:
                try:
                    del self.vertices[vertex1][vertex2]
                except KeyError as e:
                    print("Impossible to disconnect")

    def order(self):
        """
        Shows the order of the graph G. Order of a graph
        is the number of vertices of this graph.
        """
        return len(self.vertices)

    def get_vertices(self):
        """
        Get the set with the vertices of G
        """
        set_vertices = set(self.vertices.keys())
        return set_vertices

    def get_random_vertex(self):
        """
        Returns a random vertex
        """
        return choice(list(self.vertices.keys()))

    def get_adjacents(self, vertex):
        """
        Return a set with the vertex's adjacents

        :param vertex: The vertex that their adjacents
            will be added in the set.
        """
        set_adjacents = set()
        for v in self.vertices:
            if vertex in self.vertices[v]:
                set_adjacents.add(v)
        return set_adjacents

    def get_degree(self, vertex):
        """
        Get the degree of a given vertex. Degree
        of a vertex is the number of this adjacents
        vertices

        :param vetex: The vertex that the degree
            will be returned
        """
        return len(self.get_adjacents(vertex))

    ########################
    #   Specific Actions   #
    ########################
    # Actions for a specific type of graph

    def get_sucessors(self, vertex):
        """
        For directed graphs (valued or not).
        Returns a set with the sucessors vertices 
        of a given vertex

        :param vertex: Given vertex that sucessors will
            be returned.
        """
        if self.directed:
            set_sucessors = set(self.vertices[vertex].keys())
            return set_sucessors

    def get_antecessors(self, vertex):
        """
        For directed graphs (valued or not).
        Returns a set with the antecessors vertices 
        of a given vertex

        :param vertex: Given vertex that antecessors will
            be returned.
        """
        if self.directed:
            return self.get_adjacents(vertex)

    def get_outdegree(self, vertex):
        """
        For directed graphs (valued or not).
        Get the degree of emission of a given vertex

        :param vertex: The vertex that the degree of
            emission will ve returned
        """
        if self.directed:
            return len(self.vertices[vertex])

    def get_indegree(self, vertex):
        """
        For directed graphs (valued or not).
        Get the degree of reception of a given vertex

        :param vertex: The vertex that the degree of
            reception will ve returned
        """
        if self.directed:
            return len(self.get_adjacents(vertex))

    def get_value(self, vertex1, vertex2):
        """
        For valued graphs (directed or not).
        Get the value of a edge between the vertex1
        and vertex2. If G is a directed graph, such 
        that:
            A -----(5)-----> B
        if this function was called like this:
            G.get_value(A, B)
        will return 5.

        :param vertex1: A vertex.
        :param vertex2: Another vertex.
        """
        if self.valued:
            try:
                value = self.vertices[vertex1][vertex2]
            except KeyError as ke:
                print("Impossible to get the value")
            else:
                return value

    ########################
    #  Derivative Actions  #
    ########################
    # Derivative actions for a undirected graph
    # (except has_cycle)

    def is_regular(self):
        """
        Checks if the graph is a regular graph, so,
        if each vertex of G has the same degree
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

    def transitive_closure(self, vertex, visited):
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
        return (set(self.vertices.keys())) == self.transitive_closure(self.get_random_vertex(), set())

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
        for adjacent in self.get_adjacents(actual_v):
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
        return self.is_connected() and not(self.has_cycle(vertex, vertex, None))
