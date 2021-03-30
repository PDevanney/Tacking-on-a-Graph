import operator
import time

from treelib import *
from distances import *
from search import search
from datetime import datetime


# Return a Boolean value indicating if the Target has been found
# Parameters:
#   int target_location
#   List[int] visited
#   A List of dictionary distances to every node from Tower keyed by Node: distances
#   A List of dictionary distances to the every possible target from Tower keyed by Node: distance_to_target
# Output:
#   Boolean is target found
def optimal_is_found(target_location, visited, distances, distance_to_target):

    target_distance = [item[target_location] for item in distance_to_target]
    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    s = search(distances, target_distance, visited)
    return len(s) == 1


# Recursive function to create a Tree of all un-found paths of the Graph
# Parameters:
#   Graph graph
#   Tree tree
#   int node
#   String parent
#   A List of dictionary distances to every node from Tower keyed by Node: distance_table
#   List[int] tower_locations
#   A List of dictionary distances to the every possible target from Tower keyed by Node: distance_to_target
def build_tree(graph, tree, node, parent, distance_table, tower_locations, distance_to_target):
    v = [int(n) for n in parent.split(',')]

    for t in tower_locations:
        v.append(t)

    possible_moves = []
    for n in graph.neighbors(node):
        if n not in v:
            possible_moves.append(n)

    for n in possible_moves:
        ident = parent + "," + str(n)

        tree.create_node(n, ident, parent=parent)

        if not optimal_is_found(n, v, distance_table, distance_to_target):
            build_tree(graph, tree, n, parent + "," + str(n), distance_table, tower_locations, distance_to_target)


# Return the Longest Path for the given Start Location
# Parameters:
#   Graph graph
#   int target
#   List[int] tower_locations
#   A List of dictionary distances to the every possible target from Tower keyed by Node: distance_to_target
# Output:
#   Tuple (int, List[string]) : length of longest path, longest path
def optimal_path(graph, target, tower_locations, distance_to_target):
    # Create initial Tree structure with start node as the ROOT
    all_path = Tree()
    all_path.create_node(target, str(target))

    # Create the distance table for each tower
    distance_table = []
    for t in tower_locations:
        distance_table.append(populate_distance_table(graph, t))

    possible_moves = []
    for i in graph.neighbors(target):
        if i not in tower_locations:
            possible_moves.append(i)

    # Check if the root node is found
    if not optimal_is_found(target, tower_locations, distance_table, distance_to_target) and len(possible_moves) > 0:
        build_tree(graph, all_path, target, str(target), distance_table, tower_locations, distance_to_target)

    leaves = all_path.leaves()
    depth = {}
    for leaf in leaves:
        length = all_path.depth(leaf) + 1
        if length in depth.keys():
            depth[length].append(leaf.identifier)
        else:
            depth[length] = [leaf.identifier]

    longest_path = []
    longest_path_list = depth[max(depth)]

    for longest_path_string in longest_path_list:
        longest_path.append(list(map(int, longest_path_string.split(','))))

    return max(depth), longest_path


# Return the Longest Path for the given towers
# Parameters:
#   Graph graph
#   List[int] towers
# Output:
#   Tuple (int, List[string]) : length of longest path, longest path
def find_optimal_node(graph, towers):
    path_size = []

    # Calculate a List of dictionaries of the distance from the Towers to every other node keyed by Graph Node
    distance_to_target = []
    for t in towers:
        i_distance = {}
        for n in graph.nodes():
            try:
                i_distance[n] = len(nx.dijkstra_path(graph, t, n)) - 1
            except nx.NetworkXNoPath:
                i_distance[n] = -1
        distance_to_target.append(i_distance)

    for n in graph.nodes():
        if n not in towers:
            opt = optimal_path(graph, n, towers, distance_to_target)
            path_size.append(opt)

    longest_distance = max(path_size, key=operator.itemgetter(0))[0]
    return_arr = []
    for d in path_size:
        if d[0] == longest_distance:
            return_arr = return_arr + d[1]

    return longest_distance, return_arr
