import random
from itertools import combinations

import numpy as np
from distances import populate_distance_table
from movement import find_optimal_node


class RandomTower:

    @staticmethod
    def initial_position(G, tower_count):
        return random.sample(G.nodes, tower_count)


class HeuristicTower:

    @staticmethod
    def initial_position(G, tower_count):
        unique_distances = []
        for node in G.nodes:
            unique_distances.append(len(set((populate_distance_table(G, node)).values())))

        optimal = np.argpartition(unique_distances, -tower_count)[-tower_count:]
        return optimal


class OptimalTower:

    @staticmethod
    def initial_position(G, tower_count):
        # Get all possible combinations of Tower locations
        tower_combinations = combinations(list(G.nodes), tower_count)

        short_tower_path_length = len(G.nodes) + 1
        for comb in list(tower_combinations):
            # Get the longest path for the given Tower combination
            current_path_length = find_optimal_node(G, list(comb))[0] # Problem here?

            if current_path_length < short_tower_path_length:
                optimal_comb = list(comb)
                short_tower_path_length = current_path_length

        return optimal_comb
