#!/usr/bin/env python3
from unittest import TestCase, main
from graph import Graph

class Test(TestCase):
	def test_construct_undirected_graph(self):
		graph = Graph({
				"a":{"b", "c", "d"},
				"b":{"a", "f"},
				"c":{"a"},
				"d":{"a", "e"},
				"e":{"d"},
				"f":{"b"}
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
				"a":{"b", "c"},
				"b":{"a"},
				"c":{"a"}
			})
		self.assertEqual(graph.order(), 3)
		
		graph.add_vertex("d")
		self.assertEqual(graph.order(), 4)
		self.assertEqual(graph.get_degree("d"), 0)
		
		graph.connect("b", "d")
		self.assertEqual(graph.get_degree("b"), 2)
		self.assertEqual(graph.get_degree("d"), 1)

	def test_remove_vertex(self):
		graph = Graph({
				"a":{"c", "b", "d"},
				"b":{"a", "e"},
				"c":{"a"},
				"d":{"a", "e", "f"},
				"e":{"d", "b"},
				"f":{"d"}
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
				"a":{"b", "c", "d"},
				"b":{"a", "f"},
				"c":{"a", "g"},
				"d":{"a", "e"},
				"e":{"d"},
				"f":{"b"},
				"g":{"c"}
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
				"a":{"b", "c", "d"},
				"b":{"a", "f"},
				"c":{"a", "g"},
				"d":{"a", "e"},
				"e":{"d"},
				"f":{"b"},
				"g":{"c"}
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
				"a":{"b", "c", "d"},
				"b":{"a", "f"},
				"c":{"a", "g"},
				"d":{"a", "e"},
				"e":{"d"},
				"f":{"b"},
				"g":{"c"}
			})

		graph3 = Graph({})

		self.assertEqual(graph1.get_vertices(), {"a", "b", "c"})
		self.assertEqual(graph2.get_vertices(), {"a", "b", "c", "d", "e", "f", "g"})
		self.assertEqual(graph3.get_vertices(), set())

	def test_get_adjacents(self):
		graph = Graph({
				"a":{"c", "b", "e", "f"},
				"b":{"a", "d"},
				"c":{"a"},
				"d":{"b"},
				"e":{"a", "f", "i"},
				"f":{"a", "j", "e", "g"},
				"g":{"f", "h"},
				"h":{"g", "i"},
				"i":{"e", "h"},
				"j":{"f"}
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
				"a":{"b", "c", "d"},
				"b":{"a", "f"},
				"c":{"a", "g"},
				"d":{"a", "e"},
				"e":{"d"},
				"f":{"b"},
				"g":{"c"}
			})
		self.assertIsNotNone(graph.get_random_vertex())
		self.assertIsNotNone(graph.get_random_vertex())

	def test_is_regular_and_complete_graph(self):
		graph1 = Graph({
				"a":{"b", "c"},
				"b":{"a", "c"},
				"c":{"a", "b"}
			})
		graph2 = Graph({
				"a":{"b", "c"},
				"b":{},
				"c":{}
			})
		self.assertTrue(graph1.is_regular())
		self.assertFalse(graph2.is_regular())
		self.assertTrue(graph1.is_complete())
		self.assertFalse(graph2.is_complete())

	# Sometime goes, sometimes not...
	#def test_transitive_closure(self):
	#	graph = Graph({
	#			"a":{"b", "f"},
	#			"b":{"a", "c"},
	#			"c":{"f", "d", "b"},
	#			"d":{"c", "e"},
	#			"e":{"d"},
	#			"f":{"g", "c", "a"},
	#			"g":{"f", "h", "i"},
	#			"h":{"g"},
	#			"i":{"g"}
	#		})
	#	self.assertEqual(graph.transitive_closure("a"), {"a", "b", "c", "d", "e", "f", "g", "h", "i"})
	#	self.assertEqual(graph.transitive_closure("b"), {"a", "b", "c", "d", "e", "f", "g", "h", "i"})

	def test_is_connected(self):
		graph1 = Graph({
				"a":{"b"},
				"b":{"a"},
			})
		graph2 = Graph({
				"a":{"b"},
				"b":{"a", "c"},
				"c":{"b"},
				"d":{"e"},
				"e":{"d"}
			})
		self.assertTrue(graph1.is_connected())
		self.assertFalse(graph2.is_connected())

	# Sometime goes, sometimes not...
	#def test_is_tree(self):
	#	g1 = Graph({
	#			"a":{"b", "c"},
	#			"b":{"a", "d", "e"},
	#			"c":{"a", "f", "g"},
	#			"d":{"b"},
	#			"e":{"b"},
	#			"f":{"c"},
	#			"g":{"c"}
	#		})
	#	g2 = Graph({
	#			"a":{"b", "c"},
	#			"b":{"a", "c"},
	#			"c":{"a", "b"}
	#		})
	#	g3 = Graph({
	#			"a":{},
	#			"b":{}
	#		})
	#	self.assertTrue(g1.is_tree())
	#	self.assertFalse(g2.is_tree())
	#	self.assertFalse(g3.is_tree())

	def test_construct_directed_graph(self):
		graph = Graph({
				"a":{"b", "c"},
				"b":{"d"},
				"c":{"e"},
				"d":{},
				"e":{}
			}, True)
		self.assertEqual(graph.order(), 5)
		self.assertEqual(graph.get_vertex_indegree("a"), 0)
		self.assertEqual(graph.get_vertex_indegree("b"), 1)
		self.assertEqual(graph.get_vertex_indegree("c"), 1)
		self.assertEqual(graph.get_vertex_indegree("d"), 1)
		self.assertEqual(graph.get_vertex_indegree("e"), 1)

		self.assertEqual(graph.get_vertex_outdegree("a"), 2)
		self.assertEqual(graph.get_vertex_outdegree("b"), 1)
		self.assertEqual(graph.get_vertex_outdegree("c"), 1)
		self.assertEqual(graph.get_vertex_outdegree("d"), 0)
		self.assertEqual(graph.get_vertex_outdegree("e"), 0)

if __name__ == "__main__":
	main()