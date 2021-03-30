import networkx as nx

from unittest import TestCase
from context import search


class TestSearch(TestCase):

    def setUp(self):
        self.G = nx.complete_graph(4)

    def test_search_no_visited_single_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}]
        tower_to_target = [0]
        visited = []
        self.assertEqual([1], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_no_visited_single_tower_multi_possible(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}]
        tower_to_target = [1]
        visited = []
        self.assertEqual([0, 2], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_no_visited_multi_tower(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [0, 1]
        visited = []
        self.assertEqual([], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_some_visited_single_tower(self):
        target_to_every_node = [{0: 1, 1: 1, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [1, 1]
        visited = [0, 2]
        self.assertEqual([1], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_all_visited(self):
        target_to_every_node = [{0: 1, 1: 1, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [1, 1]
        visited = [0, 1, 2]
        self.assertEqual([], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_no_nodes(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [-1, -1]
        visited = [0, 1, 2]
        self.assertEqual([], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_some_possible(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [1, 1]
        visited = []
        self.assertEqual([0, 2], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_one_possible(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 0}, {0: 1, 1: 0, 2: 0}]
        tower_to_target = [1, 1]
        visited = []
        self.assertEqual([0], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_all_possible(self):
        target_to_every_node = [{0: 1, 1: 1, 2: 1}, {0: 1, 1: 1, 2: 1}]
        tower_to_target = [1, 1]
        visited = []
        self.assertEqual([0, 1, 2], search.search(target_to_every_node, tower_to_target, visited))

    def test_search_no_possible(self):
        target_to_every_node = [{0: 1, 1: 0, 2: 1}, {0: 1, 1: 0, 2: 1}]
        tower_to_target = [-1, -1]
        visited = []
        self.assertEqual([], search.search(target_to_every_node, tower_to_target, visited))


    def test_is_found(self):
        target = 0
        tower = [1, 2]
        visited = [3, 4]
        distances = [{0: 1, 1: 0, 2: 1, 3: 1}, {0: 1, 1: 1, 2: 0, 3: 1}]
        self.assertEqual(True, search.is_found(self.G, target, tower, visited, distances))

    def test_is_not_found(self):
        target = 0
        tower = [1, 2]
        visited = [3, 4]
        distances = [{0: -1, 1: 0, 2: -1, 3: -1}, {0: -1, 1: -1, 2: 0, 3: -1}]
        self.assertEqual(False, search.is_found(self.G, target, tower, visited, distances))
