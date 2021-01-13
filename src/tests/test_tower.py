import unittest
import networkx as nx
import numpy as np

from context import tower


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.random_tower = tower.RandomTower()
        self.heuristic_tower = tower.HeuristicTower()
        self.optimal_tower = tower.OptimalTower()

        self.path = nx.path_graph(5)

        self.test_graph = nx.complete_graph(3)
        self.test_graph.add_node(3)
        self.test_graph.add_edge(1, 3)
        self.tower_count = 3

    def test_random_loc_all_different(self):
        location = self.random_tower.initial_position(self.test_graph, self.tower_count)
        unique_locations = np.unique(location)
        self.assertEqual(unique_locations.size, len(location))

    def test_random_loc_correct_size(self):
        location = self.random_tower.initial_position(self.test_graph, self.tower_count)
        self.assertEqual(len(location), self.tower_count)

    def test_heuristic_path(self):
        location = self.heuristic_tower.initial_position(self.path, self.tower_count)
        self.assertCountEqual([3, 0, 4], list(location))

    def test_heuristic_graph(self):
        location = self.heuristic_tower.initial_position(self.test_graph, self.tower_count)
        self.assertCountEqual([0, 2, 3], list(location))

    def test_optimal_path_single(self):
        location = self.optimal_tower.initial_position(self.path, 1)
        self.assertCountEqual([0], list(location))

    def test_optimal_path_multi(self):
        location = self.optimal_tower.initial_position(self.path, 2)
        self.assertCountEqual([0, 1], list(location))


if __name__ == '__main__':
    unittest.main()
