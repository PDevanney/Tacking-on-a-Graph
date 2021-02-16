import random
import numpy as np
from itertools import combinations
from distances import populate_distance_table
from optimal import find_optimal_node


class RandomTower:

    # Return a random List[int] for the tower_locations
    # Parameters:
    #   Graph graph
    #   int tower_count
    # Output:
    #   List[int] tower_locations
    @staticmethod
    def initial_position(graph, tower_count, tower_location={}):
        tower_location[0] = random.sample(graph.nodes, tower_count)
        return tower_location[0]


class HeuristicTower:

    # Return a heuristically chosen value to place the towers. Based on the number of Unique Distances from each Node.
    # Parameters:
    #   Graph graph
    #   int tower_count
    # Output:
    #   List[int] tower_locations
    @staticmethod
    def initial_position(graph, tower_count, tower_location={}):
        unique_distances = []
        for node in graph.nodes:
            unique_distances.append(len(set((populate_distance_table(graph, node)).values())))

        heuristic = np.argpartition(unique_distances, -tower_count)[-tower_count:]

        tower_location[0] = heuristic
        return tower_location[0]


class OptimalTower:

    # Return the Optimal Positions to place the Towers - based on the Minimax approach
    #   Go through each combination of tower_locations.
    #   Return the longest possible path for each combination.
    #   Return the shortest path from the above output.
    # Parameters:
    #   Graph graph
    #   int tower_count
    # Output:
    #   List[int] tower_locations
    @staticmethod
    def initial_position(graph, tower_count, tower_location={}):
        # Get all possible combinations of Tower locations
        tower_combinations = combinations(list(graph.nodes), tower_count)

        short_tower_path_length = len(graph.nodes) + 1
        for comb in list(tower_combinations):
            # Get the longest path for the given Tower combination
            current_path_length = find_optimal_node(graph, list(comb))[0] # Problem here?

            if current_path_length < short_tower_path_length:
                optimal_comb = list(comb)
                short_tower_path_length = current_path_length

        tower_location[0] = optimal_comb
        return tower_location[0]
