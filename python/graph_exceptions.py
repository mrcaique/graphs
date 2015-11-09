#!/usr/bin/env python3
# Exceptions for the graph.py file, check the documentation of
# the file for more information.
#
# VertexNotFound is raised when a vertex is not presented in
# the dict with vertices of the graph (in other words, when 
# the vertex is not in self.vertices).
#
# NotDigraph is raised when the actions is executed by a undi-
# rected graph in a method specified for a digraph.
#
# NotValued is raised when the actions is executed by a non-
# valued graph in a method specified for a valued graph.
#
class VertexNotFound(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class NotDigraph(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class NotValued(Exception):
    pass
