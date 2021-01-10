import random
import numpy as np
import networkx as nx
from itertools import combinations

from distances import populate_distance_table
from movement import find_optimal_node


# Return a random integer for the target_location
# Parameters:
#   int number_of_nodes
# Output:
#   int tower_location
class RandomTarget:

    def initial_location(self, G, tower_locations):
        number_of_nodes = len(G.nodes)
        random_location = random.randrange(0, number_of_nodes)

        while random_location in tower_locations:
            random_location = random.randrange(0, number_of_nodes)

        return random_location

    def next_move(self, possible_moves, turn):
        return possible_moves[random.randrange(0, len(possible_moves))]


class HeuristicTarget:

    def initial_location(self, G, tower_locations):
        common_distances = []
        for node in G.nodes:
            common_distances.append(len(set((populate_distance_table(G, node)).values())))

        index = np.argmin(common_distances)

        while index in tower_locations:
            common_distances[index] = len(G.nodes) + 1
            index = np.argmin(common_distances)

        return index

    def next_move(self, possible_moves, turn):
        # ToDo Implement Heuristic Target Movement
        return possible_moves[random.randrange(0, len(possible_moves))]


class OptimalTarget:

    def optimal_path(self, G, tower_count):
        tower_combinations = combinations(list(G.nodes), tower_count)
        longest_path_length = -1

        for comb in list(tower_combinations):
            longest_paths = find_optimal_node(G, list(comb))

            path_length = longest_paths[0]
            if path_length > longest_path_length:
                ret_path = longest_paths[1][0]
                longest_path_length = path_length
        return ret_path


    def initial_location(self, G, longest_path):
        return longest_path[0]

    def next_move(self, longest_path, turn):
        return longest_path[turn]
