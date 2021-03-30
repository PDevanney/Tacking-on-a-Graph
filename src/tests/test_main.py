import unittest

from context import main


class TestMain(unittest.TestCase):

    def test_assign_colours(self):
        nodes = 5
        tower = [0, 1]
        target = 2
        visited = [3]
        self.assertEqual(['red', 'red', 'blue', 'green', 'gray'], main.get_node_colours(nodes, tower, target, visited))

    def test_assign_colours_nothing(self):
        nodes = 5
        tower = []
        target = -1
        visited = []
        self.assertEqual(['gray', 'gray', 'gray', 'gray', 'gray'], main.get_node_colours(nodes, tower, target, visited))


if __name__ == '__main__':
    unittest.main()
