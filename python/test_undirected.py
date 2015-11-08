#!/usr/bin/env python3
from unittest import TestCase, main
from graph import Graph
from graph_exceptions import NotDigraph, NotValued

class TestUndirected(TestCase):
    def test_construct_undirected_graph(self):
        graph = Graph({
                "a":{"b":None, "c":None, "d":None},
                "b":{"a":None, "f":None},
                "c":{"a":None},
                "d":{"a":None, "e":None},
                "e":{"d":None},
                "f":{"b":None}
            })
        self.assertEqual(graph.order(), 6)
        self.assertEqual(graph.get_degree("a"), 3)
        self.assertEqual(graph.get_degree("b"), 2)
        self.assertEqual(graph.get_degree("c"), 1)
        self.assertEqual(graph.get_degree("d"), 2)
        self.assertEqual(graph.get_degree("e"), 1)
        self.assertEqual(graph.get_degree("f"), 1)

    def test_add_vertex(self):
        graph = Graph({
                "a":{"b":None, "c":None},
                "b":{"a":None},
                "c":{"a":None}
            })
        self.assertEqual(graph.order(), 3)

        graph.add_vertex("d")
        self.assertEqual(graph.order(), 4)
        self.assertEqual(graph.get_degree("d"), 0)

        graph.connect("b", "d")
        self.assertEqual(graph.get_degree("b"), 2)
        self.assertEqual(graph.get_degree("d"), 1)

    def test_add_already_added(self):
        graph = Graph({
                "a":{"b":None, "c":None},
                "b":{"a":None},
                "c":{"a":None}
            })

        self.assertRaises(graph.add_vertex("a"))
        self.assertRaises(graph.add_vertex("b"))
        self.assertRaises(graph.add_vertex("c"))

        self.assertEqual(graph.get_vertices(), {"a", "b", "c"})

    def test_remove_vertex(self):
        graph = Graph({
                "a":{"c":None, "b":None, "d":None},
                "b":{"a":None, "e":None},
                "c":{"a":None},
                "d":{"a":None, "e":None, "f":None},
                "e":{"d":None, "b":None},
                "f":{"d":None}
            })
        self.assertEqual(graph.order(), 6)

        graph.remove_vertex("f")
        self.assertEqual(graph.get_degree("d"), 2)
        self.assertEqual(graph.get_adjacents("d"), {"e", "a"})
        
        graph.remove_vertex("a")
        self.assertEqual(graph.get_degree("c"), 0)
        self.assertEqual(graph.get_degree("b"), 1)
        self.assertEqual(graph.get_degree("d"), 1)

        self.assertEqual(graph.get_adjacents("c"), set())
        self.assertEqual(graph.get_adjacents("b"), {"e"})
        self.assertEqual(graph.get_adjacents("d"), {"e"})

    def test_connect(self):
        graph = Graph({
                "a":{},
                "b":{},
                "c":{},
                "d":{}
            })

        self.assertEqual(graph.get_degree("a"), 0)
        self.assertEqual(graph.get_degree("b"), 0)
        self.assertEqual(graph.get_degree("c"), 0)
        self.assertEqual(graph.get_degree("d"), 0)
        
        graph.connect("a", "b")
        graph.connect("c", "d")
        self.assertEqual(graph.get_degree("a"), 1)
        self.assertEqual(graph.get_degree("b"), 1)
        self.assertEqual(graph.get_degree("c"), 1)
        self.assertEqual(graph.get_degree("d"), 1)

        self.assertEqual(graph.get_adjacents("a"), {"b"})
        self.assertEqual(graph.get_adjacents("b"), {"a"})
        self.assertEqual(graph.get_adjacents("c"), {"d"})
        self.assertEqual(graph.get_adjacents("d"), {"c"})
        
        graph.connect("b", "c")
        self.assertEqual(graph.get_degree("b"), 2)
        self.assertEqual(graph.get_degree("c"), 2)
        
        self.assertEqual(graph.get_adjacents("b"), {"a", "c"})
        self.assertEqual(graph.get_adjacents("c"), {"b", "d"})

    def test_disconnect(self):
        graph = Graph({
                "a":{"b":None, "c":None, "d":None},
                "b":{"a":None, "f":None},
                "c":{"a":None, "g":None},
                "d":{"a":None, "e":None},
                "e":{"d":None},
                "f":{"b":None},
                "g":{"c":None}
            })

        graph.disconnect("a", "b")
        graph.disconnect("a", "c")
        graph.disconnect("c", "g")
        graph.disconnect("f", "b")

        self.assertEqual(graph.get_degree("a"), 1)
        self.assertEqual(graph.get_degree("b"), 0)
        self.assertEqual(graph.get_degree("c"), 0)
        self.assertEqual(graph.get_degree("d"), 2)
        self.assertEqual(graph.get_degree("e"), 1)
        self.assertEqual(graph.get_degree("f"), 0)
        self.assertEqual(graph.get_degree("g"), 0)

        self.assertEqual(graph.get_adjacents("a"), {"d"})
        self.assertEqual(graph.get_adjacents("b"), set())
        self.assertEqual(graph.get_adjacents("c"), set())
        self.assertEqual(graph.get_adjacents("d"), {"a", "e"})
        self.assertEqual(graph.get_adjacents("e"), {"d"})
        self.assertEqual(graph.get_adjacents("f"), set())
        self.assertEqual(graph.get_adjacents("g"), set())

    def test_order(self):
        graph1 = Graph({
                "a":{},
                "b":{},
                "c":{}
            })

        graph2 = Graph({
                "a":{"b":None, "c":None, "d":None},
                "b":{"a":None, "f":None},
                "c":{"a":None, "g":None},
                "d":{"a":None, "e":None},
                "e":{"d":None},
                "f":{"b":None},
                "g":{"c":None}
            })

        graph3 = Graph({})

        self.assertEqual(graph1.order(), 3)
        self.assertEqual(graph2.order(), 7)
        self.assertEqual(graph3.order(), 0)

    def test_get_vertices(self):
        graph1 = Graph({
                "a":{},
                "b":{},
                "c":{}
            })

        graph2 = Graph({
                "a":{"b":None, "c":None, "d":None},
                "b":{"a":None, "f":None},
                "c":{"a":None, "g":None},
                "d":{"a":None, "e":None},
                "e":{"d":None},
                "f":{"b":None},
                "g":{"c":None}
            })

        graph3 = Graph({})

        self.assertEqual(graph1.get_vertices(), {"a", "b", "c"})
        self.assertEqual(graph2.get_vertices(), {"a", "b", "c", "d", "e", "f", "g"})
        self.assertEqual(graph3.get_vertices(), set())

    def test_get_adjacents(self):
        graph = Graph({
                "a":{"c":None, "b":None, "e":None, "f":None},
                "b":{"a":None, "d":None},
                "c":{"a":None},
                "d":{"b":None},
                "e":{"a":None, "f":None, "i":None},
                "f":{"a":None, "j":None, "e":None, "g":None},
                "g":{"f":None, "h":None},
                "h":{"g":None, "i":None},
                "i":{"e":None, "h":None},
                "j":{"f":None}
            })

        self.assertEqual(graph.get_adjacents("a"), {"c", "b", "e", "f"})
        self.assertEqual(graph.get_adjacents("b"), {"a", "d"})
        self.assertEqual(graph.get_adjacents("c"), {"a"})
        self.assertEqual(graph.get_adjacents("d"), {"b"})
        self.assertEqual(graph.get_adjacents("e"), {"a", "f", "i"})
        self.assertEqual(graph.get_adjacents("f"), {"a", "j", "e", "g"})
        self.assertEqual(graph.get_adjacents("g"), {"f", "h"})
        self.assertEqual(graph.get_adjacents("h"), {"g", "i"})
        self.assertEqual(graph.get_adjacents("i"), {"e", "h"})
        self.assertEqual(graph.get_adjacents("j"), {"f"})

    def test_get_random(self):
        graph = Graph({
                "a":{"b":None, "c":None, "d":None},
                "b":{"a":None, "f":None},
                "c":{"a":None, "g":None},
                "d":{"a":None, "e":None},
                "e":{"d":None},
                "f":{"b":None},
                "g":{"c":None}
            })
        self.assertIsNotNone(graph.get_random_vertex())
        self.assertIsNotNone(graph.get_random_vertex())

    def test_is_regular_and_complete_graph(self):
        graph1 = Graph({
                "a":{"b":None, "c":None},
                "b":{"a":None, "c":None},
                "c":{"a":None, "b":None}
            })
        graph2 = Graph({
                "a":{"b":None, "c":None},
                "b":{},
                "c":{}
            })
        self.assertTrue(graph1.is_regular())
        self.assertFalse(graph2.is_regular())
        self.assertTrue(graph1.is_complete())
        self.assertFalse(graph2.is_complete())

    def test_transitive_closure(self):
       graph = Graph({
               "a":{"b":None, "f":None},
               "b":{"a":None, "c":None},
               "c":{"f":None, "d":None, "b":None},
               "d":{"c":None, "e":None},
               "e":{"d":None},
               "f":{"g":None, "c":None, "a":None},
               "g":{"f":None, "h":None, "i":None},
               "h":{"g":None},
               "i":{"g":None}
           })
       self.assertEqual(graph.transitive_closure("a", set()), 
            {"a", "b", "c", "d", "e", "f", "g", "h", "i"})
       self.assertEqual(graph.transitive_closure("b", set()),
            {"a", "b", "c", "d", "e", "f", "g", "h", "i"})

    def test_is_connected(self):
        graph1 = Graph({
                "a":{"b":None},
                "b":{"a":None},
            })
        graph2 = Graph({
                "a":{"b":None},
                "b":{"a":None, "c":None},
                "c":{"b":None},
                "d":{"e":None},
                "e":{"d":None}
            })
        self.assertTrue(graph1.is_connected())
        self.assertFalse(graph2.is_connected())

    def test_is_tree(self):
        g1 = Graph({
               "a":{"b":None, "c":None},
               "b":{"a":None, "d":None, "e":None},
               "c":{"a":None, "f":None, "g":None},
               "d":{"b":None},
               "e":{"b":None},
               "f":{"c":None},
               "g":{"c":None}
           })
        g2 = Graph({
               "a":{"b":None, "c":None},
               "b":{"a":None, "c":None},
               "c":{"a":None, "b":None}
           })
        g3 = Graph({
               "a":{},
               "b":{}
           })
        g4 = Graph({
                "a":{},
                "b":{"c":None, "d":None},
                "c":{"b":None, "d":None},
                "d":{"b":None, "c":None}
            })
        self.assertTrue(g1.is_tree())
        self.assertFalse(g2.is_tree())
        self.assertFalse(g3.is_tree())
        self.assertFalse(g4.is_tree())

    def test_specific_actions(self):
        g = Graph({
                "a":{"b":None},
                "b":{"a":None},
            })

        self.assertRaises(NotDigraph, g.get_successors, "a")
        self.assertRaises(NotDigraph, g.get_predecessors, "b")
        self.assertRaises(NotDigraph, g.get_indegree, "a")
        self.assertRaises(NotDigraph, g.get_outdegree, "b")
        self.assertRaises(NotValued, g.get_value, "a", "b")

if __name__ == "__main__":
    main()
