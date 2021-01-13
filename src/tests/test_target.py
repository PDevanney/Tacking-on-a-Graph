import unittest
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from context import target


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.random_target = target.RandomTarget()
        self.heuristic_target = target.HeuristicTarget()
        self.optimal_target = target.OptimalTarget()

        self.path = nx.path_graph(5)

        self.test_graph = nx.complete_graph(3)
        self.test_graph.add_node(3)
        self.test_graph.add_edge(1, 3)
        self.tower_count = 3

        self.heuristic_graph = nx.path_graph(4)
        self.heuristic_graph.add_edges_from([(0, 3), (0, 4), (1, 4), (2, 4), (3, 4)])

    def test_random_location_not_tower(self):
        towers = [0, 1, 2]
        location = self.random_target.initial_location(self.test_graph, towers)
        self.assertNotIn(location, towers)

    def test_random_location_in_graph(self):
        towers = [0]
        location = self.random_target.initial_location(self.test_graph, towers)
        self.assertIn(location, self.test_graph.nodes())

    def test_random_next_move(self):
        possible = [0, 1, 2]
        move = self.random_target.next_move(possible)
        self.assertIn(move, possible)

    def test_heuristic_location(self):
        towers = [0, 1]
        location = self.heuristic_target.initial_location(self.heuristic_graph, towers)

        self.assertEqual(location, 4)

    # ToDo Implement this Test
    def test_heuristic_next_move(self):
        towers = [0, 1]
        location = self.heuristic_target.initial_location(self.heuristic_graph, towers)

        self.assertEqual(location, 4)

    def test_optimal_location(self):
        pass

    def test_optimal_next_moves(self):
        pass

    def test_optimal_path(self):
        pass


if __name__ == '__main__':
    unittest.main()
