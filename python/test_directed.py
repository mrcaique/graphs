#!/usr/bin/env python3
from unittest import TestCase, main
from graph import Graph
from graph_exceptions import VertexNotFound, NotValued

class TestDirected(TestCase):

    def test_construct_directed_graph(self):
        graph = Graph({
                "a":{"b":None, "c":None},
                "b":{"d":None},
                "c":{"e":None},
                "d":{},
                "e":{}
            }, directed=True)
        self.assertEqual(graph.order(), 5)
        self.assertEqual(graph.get_indegree("a"), 0)
        self.assertEqual(graph.get_indegree("b"), 1)
        self.assertEqual(graph.get_indegree("c"), 1)
        self.assertEqual(graph.get_indegree("d"), 1)
        self.assertEqual(graph.get_indegree("e"), 1)

        self.assertEqual(graph.get_outdegree("a"), 2)
        self.assertEqual(graph.get_outdegree("b"), 1)
        self.assertEqual(graph.get_outdegree("c"), 1)
        self.assertEqual(graph.get_outdegree("d"), 0)
        self.assertEqual(graph.get_outdegree("e"), 0)

    def test_connect(self):
        digraph = Graph({
                "a":{},
                "b":{},
                "c":{},
                "d":{}
            }, directed=True)

        self.assertEqual(digraph.get_degree("a"), 0)
        self.assertEqual(digraph.get_degree("b"), 0)
        self.assertEqual(digraph.get_degree("c"), 0)
        self.assertEqual(digraph.get_degree("d"), 0)

        digraph.connect("a", "b")
        digraph.connect("c", "d")
        self.assertEqual(digraph.get_indegree("a"), 0)
        self.assertEqual(digraph.get_indegree("b"), 1)
        self.assertEqual(digraph.get_indegree("c"), 0)
        self.assertEqual(digraph.get_indegree("d"), 1)   

        self.assertEqual(digraph.get_outdegree("a"), 1)
        self.assertEqual(digraph.get_outdegree("b"), 0)
        self.assertEqual(digraph.get_outdegree("c"), 1)
        self.assertEqual(digraph.get_outdegree("d"), 0)

        self.assertEqual(digraph.get_successors("a"), {"b"})
        self.assertEqual(digraph.get_successors("b"), set())
        self.assertEqual(digraph.get_successors("c"), {"d"})
        self.assertEqual(digraph.get_successors("d"), set())

        self.assertEqual(digraph.get_predecessors("a"), set())
        self.assertEqual(digraph.get_predecessors("b"), {"a"})
        self.assertEqual(digraph.get_predecessors("c"), set())
        self.assertEqual(digraph.get_predecessors("d"), {"c"})

        digraph.connect("b", "c")
        self.assertEqual(digraph.get_indegree("a"), 0)
        self.assertEqual(digraph.get_indegree("b"), 1)
        self.assertEqual(digraph.get_indegree("c"), 1)
        self.assertEqual(digraph.get_indegree("d"), 1)   

        self.assertEqual(digraph.get_outdegree("a"), 1)
        self.assertEqual(digraph.get_outdegree("b"), 1)
        self.assertEqual(digraph.get_outdegree("c"), 1)
        self.assertEqual(digraph.get_outdegree("d"), 0)

        self.assertEqual(digraph.get_successors("a"), {"b"})
        self.assertEqual(digraph.get_successors("b"), {"c"})
        self.assertEqual(digraph.get_successors("c"), {"d"})
        self.assertEqual(digraph.get_successors("d"), set())

        self.assertEqual(digraph.get_predecessors("a"), set())
        self.assertEqual(digraph.get_predecessors("b"), {"a"})
        self.assertEqual(digraph.get_predecessors("c"), {"b"})
        self.assertEqual(digraph.get_predecessors("d"), {"c"})

    def test_connect_without_vertices(self):
        graph = Graph({}, directed=True)

        self.assertRaises(VertexNotFound, graph.connect, "a", "b")

    def test_connect_with_inexistent_vertex(self):
        graph = Graph({
                "a":{"b":None},
                "b":{}
            }, directed=True)

        self.assertRaises(VertexNotFound, graph.connect, "a", "c")

    def test_disconnect(self):
        digraph = Graph({
                "a":{"b":None, "c":None},
                "b":{"d":None, "e":None},
                "c":{"f":None, "g":None},
                "d":{},
                "e":{},
                "f":{},
                "g":{}
            }, directed=True)

        digraph.disconnect("a", "c")
        digraph.disconnect("b", "d")
        digraph.disconnect("c", "g")

        self.assertEqual(digraph.get_indegree("a"), 0)
        self.assertEqual(digraph.get_indegree("b"), 1)
        self.assertEqual(digraph.get_indegree("c"), 0)
        self.assertEqual(digraph.get_indegree("d"), 0)
        self.assertEqual(digraph.get_indegree("e"), 1)
        self.assertEqual(digraph.get_indegree("f"), 1)
        self.assertEqual(digraph.get_indegree("g"), 0)

        self.assertEqual(digraph.get_outdegree("a"), 1)
        self.assertEqual(digraph.get_outdegree("b"), 1)
        self.assertEqual(digraph.get_outdegree("c"), 1)
        self.assertEqual(digraph.get_outdegree("d"), 0)
        self.assertEqual(digraph.get_outdegree("e"), 0)
        self.assertEqual(digraph.get_outdegree("f"), 0)
        self.assertEqual(digraph.get_outdegree("g"), 0)

        self.assertEqual(digraph.get_successors("a"), {"b"})
        self.assertEqual(digraph.get_successors("b"), {"e"})
        self.assertEqual(digraph.get_successors("c"), {"f"})
        self.assertEqual(digraph.get_successors("d"), set())
        self.assertEqual(digraph.get_successors("e"), set())
        self.assertEqual(digraph.get_successors("f"), set())
        self.assertEqual(digraph.get_successors("g"), set())

        self.assertEqual(digraph.get_predecessors("a"), set())
        self.assertEqual(digraph.get_predecessors("b"), {"a"})
        self.assertEqual(digraph.get_predecessors("c"), set())
        self.assertEqual(digraph.get_predecessors("d"), set())
        self.assertEqual(digraph.get_predecessors("e"), {"b"})
        self.assertEqual(digraph.get_predecessors("f"), {"c"})
        self.assertEqual(digraph.get_predecessors("g"), set())

    def test_disconnect_without_vertices(self):
        graph = Graph({}, directed=True)

        self.assertRaises(VertexNotFound, graph.disconnect, "a", "b")
        self.assertRaises(VertexNotFound, graph.disconnect, "b", "c")

    def test_disconnect_with_inexistent_vertex(self):
        graph = Graph({
                "a":{"b":None},
                "b":{}
            }, directed=True)

        self.assertRaises(VertexNotFound, graph.disconnect, "a", "c")
        self.assertRaises(KeyError, graph.disconnect("b", "a"))

    def test_has_cycle(self):
        dg1 = Graph({
                "a":{"b":None, "c":None},
                "b":{"d":None, "e":None},
                "c":{"f":None, "g":None},
                "d":{},
                "e":{},
                "f":{},
                "g":{}
            }, directed=True)

        dg2 = Graph({
                "a":{"b":None},
                "b":{"c":None},
                "c":{"a":None}
            }, directed=True) 

        random_dg1 = dg1.get_random_vertex()
        random_dg2 = dg2.get_random_vertex()
        self.assertFalse(dg1.has_cycle(random_dg1, random_dg1, None))
        self.assertTrue(dg2.has_cycle(random_dg2, random_dg2, None))

    def test_specific_actions(self):
        g = Graph({
                "a":{"b":None},
                "b":{},
            }, directed=True)

        self.assertRaises(NotValued, g.get_value, "a", "b")

if __name__ == "__main__":
    main()
