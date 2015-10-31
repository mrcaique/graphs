#!/usr/bin/env python3
from unittest import TestCase, main
from graph import Graph

class TestDirected(TestCase):

    def test_construct_directed_graph(self):
        graph = Graph({
                "a":{"b":None, "c":None},
                "b":{"d":None},
                "c":{"e":None},
                "d":{},
                "e":{}
            }, True)
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
            }, True)

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

        self.assertEqual(digraph.get_sucessors("a"), {"b"})
        self.assertEqual(digraph.get_sucessors("b"), set())
        self.assertEqual(digraph.get_sucessors("c"), {"d"})
        self.assertEqual(digraph.get_sucessors("d"), set())

        self.assertEqual(digraph.get_antecessors("a"), set())
        self.assertEqual(digraph.get_antecessors("b"), {"a"})
        self.assertEqual(digraph.get_antecessors("c"), set())
        self.assertEqual(digraph.get_antecessors("d"), {"c"})

        digraph.connect("b", "c")
        self.assertEqual(digraph.get_indegree("a"), 0)
        self.assertEqual(digraph.get_indegree("b"), 1)
        self.assertEqual(digraph.get_indegree("c"), 1)
        self.assertEqual(digraph.get_indegree("d"), 1)   

        self.assertEqual(digraph.get_outdegree("a"), 1)
        self.assertEqual(digraph.get_outdegree("b"), 1)
        self.assertEqual(digraph.get_outdegree("c"), 1)
        self.assertEqual(digraph.get_outdegree("d"), 0)

        self.assertEqual(digraph.get_sucessors("a"), {"b"})
        self.assertEqual(digraph.get_sucessors("b"), {"c"})
        self.assertEqual(digraph.get_sucessors("c"), {"d"})
        self.assertEqual(digraph.get_sucessors("d"), set())

        self.assertEqual(digraph.get_antecessors("a"), set())
        self.assertEqual(digraph.get_antecessors("b"), {"a"})
        self.assertEqual(digraph.get_antecessors("c"), {"b"})
        self.assertEqual(digraph.get_antecessors("d"), {"c"})

    def test_connect_without_vertices(self):
        graph = Graph()

        self.assertRaises(graph.connect("a", "b"))

    def test_connect_with_inexistent_vertex(self):
        graph = Graph({
                "a":{"b":None},
                "b":{}
            })

        self.assertRaises(graph.connect("a", "c"))
        self.assertRaises(graph.connect("b", "a"))

    def test_disconnect(self):
        digraph = Graph({
                "a":{"b":None, "c":None},
                "b":{"d":None, "e":None},
                "c":{"f":None, "g":None},
                "d":{},
                "e":{},
                "f":{},
                "g":{}
            }, True)

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

        self.assertEqual(digraph.get_sucessors("a"), {"b"})
        self.assertEqual(digraph.get_sucessors("b"), {"e"})
        self.assertEqual(digraph.get_sucessors("c"), {"f"})
        self.assertEqual(digraph.get_sucessors("d"), set())
        self.assertEqual(digraph.get_sucessors("e"), set())
        self.assertEqual(digraph.get_sucessors("f"), set())
        self.assertEqual(digraph.get_sucessors("g"), set())

        self.assertEqual(digraph.get_antecessors("a"), set())
        self.assertEqual(digraph.get_antecessors("b"), {"a"})
        self.assertEqual(digraph.get_antecessors("c"), set())
        self.assertEqual(digraph.get_antecessors("d"), set())
        self.assertEqual(digraph.get_antecessors("e"), {"b"})
        self.assertEqual(digraph.get_antecessors("f"), {"c"})
        self.assertEqual(digraph.get_antecessors("g"), set())

    def test_disconnect_without_vertices(self):
        graph = Graph({}, True)

        self.assertRaises(graph.disconnect("a", "b"))
        self.assertRaises(graph.disconnect("b", "c"))

    def test_disconnect_with_inexistent_vertex(self):
        graph = Graph({
                "a":{"b":None},
                "b":{}
            }, True)

        self.assertRaises(graph.disconnect("a", "c"))
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
            }, True)

        dg2 = Graph({
                "a":{"b":None},
                "b":{"c":None},
                "c":{"a":None}
            }, True) 

        random_dg1 = dg1.get_random_vertex()
        random_dg2 = dg2.get_random_vertex()
        self.assertFalse(dg1.has_cycle(random_dg1, random_dg1, None))
        self.assertTrue(dg2.has_cycle(random_dg2, random_dg2, None))

if __name__ == "__main__":
    main()
