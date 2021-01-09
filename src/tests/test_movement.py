import unittest
import networkx as nx

from treelib import *
from src.tests.context import movement


class TestMovement(unittest.TestCase):

    def setUp(self):
        self.G = nx.complete_graph(4)
        self.small = nx.complete_graph(3)
        self.xsmall = nx.complete_graph(2)

    def test_is_found(self):
        target = 0
        tower = [1, 2]
        visited = [3, 4]
        distances = [{0: 1, 1: 0, 2: 1, 3: 1}, {0: 1, 1: 1, 2: 0, 3: 1}]
        self.assertEqual(True, movement.is_found(self.G, target, tower, visited, distances))

    def test_is_not_found(self):
        target = 0
        tower = [1, 2]
        visited = [3, 4]
        distances = [{0: -1, 1: 0, 2: -1, 3: -1}, {0: -1, 1: -1, 2: 0, 3: -1}]
        self.assertEqual(False, movement.is_found(self.G, target, tower, visited, distances))

    def test_optimal_path_no_tower(self):
        target = 0
        towers = []
        self.assertEqual((3, [['0', '1', '2'], ['0', '2', '1']]), movement.optimal_path(self.small, target, towers))

    def test_optimal_path_tower(self):
        target = 0
        towers = [1]
        self.assertEqual((2, [['0', '2']]), movement.optimal_path(self.small, target, towers))

    def test_optimal_path_towers(self):
        target = 0
        towers = [1, 2]
        self.assertEqual((1, [['0']]), movement.optimal_path(self.small, target, towers))

    def test_find_optimal_node(self):
        towers = []
        self.assertEqual((2, [[['0', '1']], [['1', '0']]]), movement.find_optimal_node(self.xsmall, towers))


if __name__ == '__main__':
    unittest.main()
