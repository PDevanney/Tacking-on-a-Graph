from src.distances import *
from src.search import *


def search_driver(G, target_location, tower_locations, visited_nodes, distance_to_all):
    distance_to_target = []
    for t in tower_locations:
        distance_to_target.append(current_distance_to_target(G, t, target_location))

    possible_nodes = search(distance_to_all, distance_to_target, visited_nodes)

    return possible_nodes
