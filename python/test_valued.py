#!/usr/bin/env python3
from unittest import TestCase, main
from graph import Graph

class TestValued(TestCase):
    def test_construct_valued_undirected(self):
        graph = Graph({
                "a":{"b":2, "c":3},
                "b":{"a":2, "c":6},
                "c":{"a":3, "b":6},
            }, False, True)

        self.assertEqual(graph.get_value("a", "b"), 2)
        self.assertEqual(graph.get_value("a", "c"), 3)
        self.assertEqual(graph.get_value("b", "c"), 6)
        self.assertRaises(KeyError, graph.get_value("a", "d"))

    def test_construct_valued_directed(self):
        dg = Graph({
                "a":{"b":3},
                "b":{"c":4},
                "c":{"a":2}
            }, True, True)

        self.assertEqual(dg.get_value("a", "b"), 3)
        self.assertEqual(dg.get_value("b", "c"), 4)
        self.assertEqual(dg.get_value("c", "a"), 2)

if __name__ == "__main__":
    main()
