import random
import numpy as np
import networkx as nx
from itertools import combinations

from distances import populate_distance_table
from movement import find_optimal_node, is_found


# Return a random integer for the target_location
# Parameters:
#   int number_of_nodes
# Output:
#   int tower_location
class RandomTarget:

    @staticmethod
    def initial_location(G, tower_locations):
        number_of_nodes = len(G.nodes)
        random_location = random.randrange(0, number_of_nodes)

        while random_location in tower_locations:
            random_location = random.randrange(0, number_of_nodes)

        return random_location

    @staticmethod
    def next_move(possible_moves, turn=-1):
        return possible_moves[random.randrange(0, len(possible_moves))]


class HeuristicTarget:

    @staticmethod
    def initial_location(G, tower_locations):
        common_distances = []
        for node in G.nodes:
            common_distances.append(len(set((populate_distance_table(G, node)).values())))

        index = np.argmin(common_distances)

        while index in tower_locations:
            common_distances[index] = len(G.nodes) + 1
            index = np.argmin(common_distances)

        return index

    @staticmethod
    def heuristic_target_next_move(graph, towers, visited, distances, possible_moves):
        one_step = []
        two_step = []

        for move in possible_moves:
            if not is_found(graph, move, towers, visited, distances):
                one_step.append(move)
                for neighbour in [x for x in graph.neighbors(move) if x not in visited]:
                    if not is_found(graph, neighbour, towers, visited+[move], distances):
                        two_step.append(move)
                        break

        if len(one_step) > 0:
            if len(two_step) > 0:
                return random.choice(two_step)
            return random.choice(one_step)
        return random.choice(possible_moves)


class OptimalTarget:

    @staticmethod
    def optimal_path(G, towers):
        return find_optimal_node(G, towers)[1][0]


    @staticmethod
    def initial_location(G, longest_path):
        return longest_path[0]

    @staticmethod
    def next_move(longest_path, turn):
        return longest_path[turn]
