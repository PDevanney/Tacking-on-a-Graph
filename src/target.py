import random
import numpy as np
import networkx as nx
from distances import populate_distance_table
from optimal import find_optimal_node
from playable import is_found


class RandomTarget:

    # Return a random integer for the target_location
    # Parameters:
    #   Graph graph
    #   int tower_locations
    # Output:
    #   int target_location
    @staticmethod
    def initial_location(graph, tower_locations):
        number_of_nodes = len(graph.nodes)
        random_location = random.randrange(0, number_of_nodes)

        while random_location in tower_locations:
            random_location = random.randrange(0, number_of_nodes)

        return random_location

    # Return a random integer for the next target move
    # Parameters:
    #   List[int] possible_moves
    # Output:
    #   int next_move
    @staticmethod
    def next_move(possible_moves, turn=-1):
        return possible_moves[random.randrange(0, len(possible_moves))]


class HeuristicTarget:

    # Return a heuristically chosen value to place the target. Based on the number of Unique Distances from that Node.
    # Parameters:
    #   Graph graph
    #   List[int] tower_locations
    # Output:
    #   int initial_location
    @staticmethod
    def initial_location(graph, tower_locations):
        common_distances = []
        for node in graph.nodes:
            common_distances.append(len(set((populate_distance_table(graph, node)).values())))

        index = np.argmin(common_distances)

        while index in tower_locations:
            common_distances[index] = len(graph.nodes) + 1
            index = np.argmin(common_distances)

        return index

    # Return a heuristically chosen value to move the target to.
    #   If the target can move to a neighbour and not be found (1-step neighbour) then move to neighbour of that node
    #   and not be found (2-step neighbour) Return a 2-step neighbour if one exists.
    # Parameters:
    #   Graph graph
    #   List[int] towers
    #   List[int] visited
    #   List[int] possible_moves
    # Output:
    #   int next_move
    @staticmethod
    def heuristic_target_next_move(graph, towers, visited, distances, possible_moves):
        one_step = []
        two_step = []

        for move in possible_moves:
            if not is_found(graph, move, towers, visited, distances):
                one_step.append(move)

                possible = []
                for node in graph.neighbors(move):
                    if node not in visited:
                        possible.append(node)

                for neighbour in possible:
                    if not is_found(graph, neighbour, towers, visited+[move], distances):
                        two_step.append(move)
                        break

        if len(one_step) > 0:
            if len(two_step) > 0:
                return random.choice(two_step)
            return random.choice(one_step)
        return random.choice(possible_moves)


class OptimalTarget:
    # Call the Optimal Node function to get the Longest path for a given Graph and set of Towers
    # Parameters:
    #   Graph graph
    #   List[int] towers
    # Output:
    #   List[string] longest_path
    @staticmethod
    def optimal_path(graph, towers):
        print(find_optimal_node(graph, towers))
        return find_optimal_node(graph, towers)[1][0]

    # Return the initial location of the Optimal Path - first value of the List
    # Parameters:
    #   Graph graph
    #   List[int] longest_path
    # Output:
    #   int initial_location
    @staticmethod
    def initial_location(graph, longest_path):
        return longest_path[0]

    # Return the next move for the target to take
    # Parameters:
    #   List[int] longest_path
    #   int turn
    # Output:
    #   int next_move
    @staticmethod
    def next_move(longest_path, turn):
        return longest_path[turn]
