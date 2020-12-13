import random

import numpy as np

from src.distances import populate_distance_table
from itertools import combinations
import networkx as nx




# Return an Array of unique integers
# Parameters:
#   int tower_count
#   int number_of_nodes
#   int target_location
# Output:
#   Array[int] tower_location
from src.optimal_movement import find_optimal_node


def get_tower_locations(tower_count, number_of_nodes, target_location):
    tower_location = []
    while len(tower_location) != tower_count:
        position = random.randrange(0, number_of_nodes)
        if position != target_location and position not in tower_location:
            tower_location.append(position)
    return tower_location


# Return a random integer for the target_location
# Parameters:
#   int number_of_nodes
# Output:
#   int tower_location
def get_target_location(number_of_nodes):
    return random.randrange(0, number_of_nodes)


# Return an Array of optimal tower_locations
# Parameters:
#   Graph G
# Output:
#   Array[int] tower_location
def get_optimal_tower_locations(G, tower_count, target_location):
    unique_distances = []
    for node in G.nodes:
        unique_distances.append(len(set((populate_distance_table(G, node)).values())))

    optimal = []
    while len(optimal) != tower_count:
        optimal_index = np.argmax(unique_distances)

        if optimal_index != target_location:
            optimal.append(optimal_index)
            unique_distances[optimal_index] = -1
    return optimal


def heuristic_optimal_location(G, tower_count):
    tower_combinations = combinations(list(G.nodes), tower_count)

    optimal_tower = len(G.nodes) + 1

    for comb in list(tower_combinations):
        path_length = find_optimal_node(G, list(comb))[0]

        if path_length < optimal_tower:
            optimal_comb = list(comb)
            optimal_tower = path_length

    return optimal_comb
