import operator
import time

from treelib import *
from distances import *
from search import search
from datetime import datetime

def is_found(target, visited, distances, distance_to_target):

    target_distance = [item[target] for item in distance_to_target]
    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    s = search(distances, target_distance, visited)
    return len(s) == 1

def optimal_is_found(target, visited, distances, distance_to_target):

    target_distance = [item[target] for item in distance_to_target]
    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    s = search(distances, target_distance, visited)
    return len(s) == 1


def build_tree(graph, tree, node, parent, distance_table, towers, distance_to_target):
    v = [int(n) for n in parent.split(',')] + towers

    possible_moves = []
    for n in graph.neighbors(node):
        if n not in v:
            possible_moves.append(n)

    for n in possible_moves:
        ident = parent + "," + str(n)

        tree.create_node(n, ident, parent=parent)

        if not optimal_is_found(n, v, distance_table, distance_to_target):
            # print(graph.number_of_nodes(), "\t", n, "\t", tree.depth(), "\t", parent)
            build_tree(graph, tree, n, parent + "," + str(n), distance_table, towers, distance_to_target)


def optimal_path(graph, target, towers, distance_to_target):
    # Create initial Tree structure with start node as the ROOT
    all_path = Tree()
    all_path.create_node(target, str(target))

    # Create the distance table for each tower
    distance_table = []
    for t in towers:
        distance_table.append(populate_distance_table(graph, t))

    possible_moves = []
    for i in graph.neighbors(target):
        if i not in towers:
            possible_moves.append(i)

    # Check if the root node is found
    if not optimal_is_found(target, towers, distance_table, distance_to_target) and len(possible_moves) > 0:
        build_tree(all_path, str(target), distance_table, towers, distance_to_target)

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
        longest_path.append(longest_path_string.split(','))

    return max(depth), longest_path


# Return the longest path(s) for given Towers
def find_optimal_node(graph, towers):
    path_size = []

    distance_to_target = calculate_pre_distance(graph, towers)

    start_time = datetime.now()

    for n in graph.nodes():
        if n not in towers:
            opt = optimal_path(graph, n, towers, distance_to_target)
            path_size.append(opt)

            elapsed = datetime.now() - start_time
            if (elapsed.total_seconds()/60) > 5:
                print("Current Node : ", n, " Elapsed Time : ", elapsed)  # time object

    longest_distance = max(path_size, key=operator.itemgetter(0))[0]

    return_arr = []
    for d in path_size:
        if d[0] == longest_distance:
            return_arr = return_arr + (d[1])
    return longest_distance, return_arr


def calculate_pre_distance(graph, towers):
    distance = []
    for t in towers:
        i_distance = {}
        for n in graph.nodes():
            try:
                i_distance[n] = len(nx.dijkstra_path(graph, t, n)) - 1
            except nx.NetworkXNoPath:
                i_distance[n] = -1
        distance.append(i_distance)
    return distance
