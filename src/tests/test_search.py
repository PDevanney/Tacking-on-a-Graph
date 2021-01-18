import networkx as nx

from unittest import TestCase
from src.tests.context import search


class TestSearch(TestCase):

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

    # ToDo Check Logic of this Test -- Should it return []
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
