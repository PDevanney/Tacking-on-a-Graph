import random
from itertools import combinations

import numpy as np
from distances import populate_distance_table
from movement import find_optimal_node


class RandomTower:

    def initial_position(self, G, tower_count):
        return random.sample(G.nodes, tower_count)


class HeuristicTower:
    # ind = np.argpartition(a, -4)[-4:]
    def initial_position(self, G, tower_count):
        unique_distances = []
        for node in G.nodes:
            unique_distances.append(len(set((populate_distance_table(G, node)).values())))

        # optimal = []
        #while len(optimal) != tower_count:
        #    optimal_index = np.argmax(unique_distances)

        #    if optimal_index != target_location:
        #        optimal.append(optimal_index)
        #        unique_distances[optimal_index] = -1

        optimal = np.argpartition(unique_distances, -tower_count)[-tower_count:]
        return optimal


class OptimalTower:

    def initial_position(self, G, tower_count):
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
