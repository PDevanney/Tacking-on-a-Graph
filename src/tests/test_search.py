import networkx as nx

from unittest import TestCase
from src.tests.context import search


class TestSearch(TestCase):

    def setUp(self):
        # Create a Pappus Graph +  Add a node to Simulate a disconnected Graph
        self.G = nx.pappus_graph()
        self.G.add_node(43)

    def test_optimal_possible_nodes(self):
        last_target_location = 1
        confirmed = [7, 8, 9, 10, 11, 12]
        turn = 1
        optimal = search.optimal_possible_nodes(self.G, last_target_location, confirmed, turn)

        self.assertEqual(optimal, [8])

    def test_optimal_possible_nodes_turn0(self):
        last_target_location = 1
        confirmed = [7, 8, 9, 10, 11, 12]
        turn = 0
        optimal = search.optimal_possible_nodes(self.G, last_target_location, confirmed, turn)

        self.assertEqual(optimal, confirmed)

    def test_get_possible_nodes_no_visited_single_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}]
        tower_to_target = [0]
        self.assertEqual([[1]], search.get_possible_nodes(target_to_every_node, tower_to_target, []))

    def test_get_possible_nodes_no_visited_multi_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [0, 1]
        self.assertEqual([[1], [0, 2]], search.get_possible_nodes(target_to_every_node, tower_to_target, []))

    def test_get_possible_nodes_some_visited_single_tower(self):
        target_to_every_node = [{0: 1, 1: 1, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [1, 1]
        self.assertEqual([[1], []], search.get_possible_nodes(target_to_every_node, tower_to_target, [0, 2]))

    def test_get_possible_nodes_all_visited(self):
        target_to_every_node = [{0: 1, 1: 1, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [1, 1]
        self.assertEqual([[], []], search.get_possible_nodes(target_to_every_node, tower_to_target, [0, 1, 2]))

    def test_get_possible_nodes_no_nodes(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [-1, -1]
        self.assertEqual([[], []], search.get_possible_nodes(target_to_every_node, tower_to_target, [0, 1, 2]))

    def test_confirmed_node_confirmation_1_item(self):
        pass

    def test_confirmed_node_no_confirmation(self):
        pass

    def test_confirmed_node_empty(self):
        pass