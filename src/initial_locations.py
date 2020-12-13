import random

import numpy as np

from src.distances import populate_distance_table
from itertools import combinations
import networkx as nx
from src.movement import find_optimal_node


# Return an Array of unique integers
# Parameters:
#   int tower_count
#   int number_of_nodes
#   int target_location
# Output:
#   Array[int] tower_location
def random_tower_location(tower_count, number_of_nodes):
    tower_location = []
    while len(tower_location) != tower_count:
        position = random.randrange(0, number_of_nodes)
        if position not in tower_location:
            tower_location.append(position)
    return tower_location


# Return a random integer for the target_location
# Parameters:
#   int number_of_nodes
# Output:
#   int tower_location
def random_target_location(number_of_nodes, tower_locations):
    random_location = random.randrange(0, number_of_nodes)

    while random_location in tower_locations:
        random_location = random.randrange(0, number_of_nodes)

    return random_location


def heuristic_target_location(G):
    common_distances = []
    for node in G.nodes:
        common_distances.append(len(set((populate_distance_table(G, node)).values())))

    return np.argmin(common_distances)


# Return an Array of optimal tower_locations
# Parameters:
#   Graph G
# Output:
#   Array[int] tower_location
def heuristic_tower_location(G, tower_count, target_location):
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


def optimal_tower_location(G, tower_count):
    tower_combinations = combinations(list(G.nodes), tower_count)

    optimal_tower = len(G.nodes) + 1

    for comb in list(tower_combinations):
        path_length = find_optimal_node(G, list(comb))[0]

        if path_length < optimal_tower:
            optimal_comb = list(comb)
            optimal_tower = path_length

    return optimal_comb


def optimal_target_location(G, tower_count):
    tower_combinations = combinations(list(G.nodes), tower_count)
    longest_path_length = -1

    for comb in list(tower_combinations):
        optimal_node = find_optimal_node(G, list(comb))

        if optimal_node[0] > longest_path_length:
            optimal_target = optimal_node[1][0][0][0]
            longest_path_length = optimal_node[0]

    return optimal_target
