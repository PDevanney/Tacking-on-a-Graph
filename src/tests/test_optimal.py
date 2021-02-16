import unittest
import networkx as nx

from src.tests.context import optimal


def get_distance(g, towers):
    distance_to_target = []
    for t in towers:
        i_distance = {}
        for n in g.nodes():
            try:
                i_distance[n] = len(nx.dijkstra_path(g, t, n)) - 1
            except nx.NetworkXNoPath:
                i_distance[n] = -1
        distance_to_target.append(i_distance)

    return distance_to_target


class TestOptimal(unittest.TestCase):

    def setUp(self):
        self.G = nx.complete_graph(4)
        self.small = nx.complete_graph(3)
        self.xsmall = nx.complete_graph(2)

        self.test_graph = nx.Graph()
        self.test_graph.add_nodes_from([1, 10])
        self.test_graph.add_node(100)
        self.test_graph.add_edges_from(
            [(1, 2), (2, 3), (3, 4), (4, 5), (3, 100),
             (6, 7), (7, 100), (100, 8), (8, 9), (9, 10)]
        )

    def test_optimal_is_found(self):
        target = 0
        visited = [3, 4]
        distances = [{0: 1, 1: 0, 2: 1, 3: 1}, {0: 1, 1: 1, 2: 0, 3: 1}]
        distance_to_target = get_distance(self.G, [1, 2])

        self.assertEqual(True, optimal.optimal_is_found(target, visited, distances, distance_to_target))

    def test_optimal_is_not_found(self):
        target = 0
        visited = [3, 4]
        distances = [{0: -1, 1: 0, 2: -1, 3: -1}, {0: -1, 1: -1, 2: 0, 3: -1}]
        distance_to_target = get_distance(self.G, [1, 2])

        self.assertEqual(False, optimal.optimal_is_found(target, visited, distances, distance_to_target))

    def test_optimal_path_no_tower(self):
        target = 0
        towers = []

        distance_to_target = get_distance(self.small, towers)

        self.assertEqual((3, [[0, 1, 2], [0, 2, 1]]),
                         optimal.optimal_path(self.small, target, towers, distance_to_target))

    def test_optimal_path_tower(self):
        target = 0
        towers = [1]

        distance_to_target = get_distance(self.small, towers)

        self.assertEqual((2, [[0, 2]]), optimal.optimal_path(self.small, target, towers, distance_to_target))

    def test_optimal_path_towers(self):
        target = 0
        towers = [1, 2]

        distance_to_target = get_distance(self.small, towers)

        self.assertEqual((1, [[0]]), optimal.optimal_path(self.small, target, towers, distance_to_target))

    def test_find_optimal_node_no_tower(self):
        towers = []
        self.assertEqual((2, [[0, 1], [1, 0]]), optimal.find_optimal_node(self.xsmall, towers))

    def test_find_optimal_node_tower(self):
        towers = [100]
        self.assertEqual((5, [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]),
                         optimal.find_optimal_node(self.test_graph, towers))


if __name__ == '__main__':
    unittest.main()
