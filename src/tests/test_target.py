import unittest
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from context import target


class TestTarget(unittest.TestCase):

    def setUp(self):
        self.random_target = target.RandomTarget()
        self.heuristic_target = target.HeuristicTarget()
        self.optimal_target = target.OptimalTarget()

        self.path = nx.path_graph(5)

        self.test_graph = nx.complete_graph(3)
        self.test_graph.add_node(3)
        self.test_graph.add_edge(1, 3)
        self.tower_count = 3

        self.heuristic_loc_graph = nx.path_graph(4)
        self.heuristic_loc_graph.add_edges_from([(0, 3), (0, 4), (1, 4), (2, 4), (3, 4)])

        self.heuristic_move_graph = nx.path_graph(3)

        self.target_test_graph = nx.Graph()

        self.target_test_graph.add_nodes_from([1, 10])
        self.target_test_graph.add_node(100)

        self.target_test_graph.add_edges_from(
            [(1, 2), (2, 3), (3, 4), (4, 5), (3, 100), (6, 7), (7, 100), (100, 8), (8, 9), (9, 10)])

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
        location = self.heuristic_target.initial_location(self.heuristic_loc_graph, towers)

        self.assertEqual(location, 4)

    def test_heuristic_location_not_tower(self):
        towers = [0, 1, 4]
        location = self.heuristic_target.initial_location(self.heuristic_loc_graph, towers)

        self.assertEqual(location, 2)

    def test_heuristic_next_move_0_step_single(self):
        graph = self.heuristic_move_graph
        towers = [0]
        visited = [2]
        distances = [{0: 0, 1: 1, 2: 2}]
        possible_moves = [1]

        next_move = self.heuristic_target.heuristic_target_next_move(graph, towers, visited, distances, possible_moves)

        self.assertEqual(next_move, 1)

    def test_heuristic_next_move_0_step_multi(self):
        graph = self.heuristic_move_graph
        graph.add_nodes_from([3, 4])
        graph.add_edges_from([(1, 3), (3, 4), (2, 4)])

        towers = [0]
        visited = [2]
        distances = [{0: 0, 1: 1, 2: 2, 3: 2, 4: 3}]
        possible_moves = [1, 4]

        next_move = self.heuristic_target.heuristic_target_next_move(graph, towers, visited, distances, possible_moves)
        self.assertIn(next_move, [1, 4])

    def test_heuristic_next_move_1_step_single(self):
        graph = self.heuristic_move_graph
        graph.add_nodes_from([3, 4])
        graph.add_edges_from([(1, 3), (3, 4), (2, 4), (1, 3)])

        towers = [0]
        visited = [2]
        distances = [{0: 0, 1: 1, 2: 2, 3: 2, 4: 2}]
        possible_moves = [1, 4]

        next_move = self.heuristic_target.heuristic_target_next_move(graph, towers, visited, distances, possible_moves)

        self.assertEqual(next_move, 4)

    def test_heuristic_next_move_2_step(self):
        graph = self.heuristic_move_graph
        graph.add_nodes_from([3, 4, 5])
        graph.add_edges_from([(2, 3), (2, 4), (2, 5), (4, 5)])

        towers = [0]
        visited = [2]
        distances = [{0: 0, 1: 1, 2: 2, 3: 3, 4: 3, 5: 3}]
        possible_moves = [1, 3, 4, 5]

        next_move = self.heuristic_target.heuristic_target_next_move(graph, towers, visited, distances, possible_moves)

        self.assertIn(next_move, [4, 5])

    def test_optimal_location(self):
        longest_path = [0, 1, 2, 3, 4, 5]
        location = self.optimal_target.initial_location(self.target_test_graph, longest_path)

        self.assertEqual(location, 0)

    def test_optimal_next_moves(self):
        longest_path = [0, 1, 2, 3, 4, 5]
        next_move = self.optimal_target.next_move(longest_path, 5)

        self.assertEqual(next_move, 5)

    def test_optimal_path(self):
        optimal_path = self.optimal_target.optimal_path(self.target_test_graph, 1)

        self.assertEqual(optimal_path, [1, 2, 3, 4, 5])



if __name__ == '__main__':
    unittest.main()
