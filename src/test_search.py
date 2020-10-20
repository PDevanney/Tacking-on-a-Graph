import networkx as nx

from unittest import TestCase
from search import *


class Test(TestCase):

    def setUp(self):
        # Create a Pappus Graph +  Add a node to Simulate a disconnected Graph
        self.G = nx.pappus_graph()
        self.G.add_node(43)

        self.C = nx.complete_graph(3)

    def test_optimal_possible_nodes(self):
        self.fail()

    def test_get_possible_nodes_no_visited_single_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}]
        tower_to_target = [0]
        self.assertEqual([[1]], get_possible_nodes(target_to_every_node, tower_to_target, []))

    def test_get_possible_nodes_no_visited_multi_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [0, 1]
        self.assertEqual([[1], [0, 2]], get_possible_nodes(target_to_every_node, tower_to_target, []))

    def test_get_possible_nodes_some_visited_single_tower(self):
        pass

    def test_get_possible_nodes_all_visited(self):
        pass

    def test_get_possible_nodes_no_nodes(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [-1, -1]
        self.assertEqual([], get_possible_nodes(target_to_every_node, tower_to_target, [0, 1, 2]))

    def test_confirmed_node(self):
        self.fail()
