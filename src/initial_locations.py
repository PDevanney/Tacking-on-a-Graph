import random

import numpy as np

from distances import populate_distance_table


# Return an Array of unique integers
# Parameters:
#   int tower_count
#   int number_of_nodes
#   int target_location
# Output:
#   Array[int] tower_location
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
def get_optimal_tower_locations(G, tower_count):
    unique_distances = []
    for node in G.nodes:
        unique_distances.append(len(set((populate_distance_table(G, node)).values())))

    optimal = []
    for i in range(tower_count):
        print(np.argmax(unique_distances))
        optimal.append(np.argmax(unique_distances))
        unique_distances[np.argmax(unique_distances)] = -1

    return optimal
