import unittest

import networkx as nx
import numpy as np
from unittest import TestCase
from context import distances


class TestDistances(TestCase):

    def setUp(self):
        # Create a Pappus Graph +  Add a node to Simulate a disconnected Graph
        self.G = nx.pappus_graph()
        self.G.add_node(43)
        self.C = nx.complete_graph(3)

    def test_current_distance_to_target_connected(self):
        d = distances.current_distance_to_target(self.G, 1, 3)
        self.assertEqual(2, d)

    def test_current_distance_to_target_disconnected(self):
        d = distances.current_distance_to_target(self.G, 1, 43)
        self.assertEqual(-1, d)

    def test_populate_distance_table(self):
        t = distances.populate_distance_table(self.G, 1)
        tt = {0: 1, 1: 0, 2: 1, 3: 2, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, 10: 3, 11: 4, 12: 3, 13: 2, 14: 3, 15: 4,
              16: 3, 17: 2, 43: -1}
        self.assertEqual(tt, t)

    def test_populate_distance_table_connected(self):
        t = distances.populate_distance_table(self.C, 1)
        tt = {0: 1, 1: 0, 2: 1}
        self.assertEqual(tt, t)

    def test_populate_distance_table_disconnected(self):
        self.C.add_node(3)
        t = distances.populate_distance_table(self.C, 1)
        tt = {0: 1, 1: 0, 2: 1, 3: -1}
        self.assertEqual(tt, t)


if __name__ == '__main__':
    unittest.main()
