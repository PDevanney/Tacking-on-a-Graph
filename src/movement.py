import operator
from treelib import *

from distances import *
from search import search


# ToDo Improve this code
def is_found(graph, target, tower, visited, distances):
    distance_to_target = []
    for t in tower:
        distance_to_target.append(current_distance_to_target(graph, t, target))

    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    s = search(distances, distance_to_target, visited)
    return len(s) == 1


def build_tree(G, t, node, parent, distance_table, towers):
    v = [int(n) for n in parent.split(',')]

    for tower in towers:
        v.append(tower)

    for n in G.neighbors(node):
        if n not in v:
            ident = parent + "," + str(n)

            t.create_node(n, ident, parent=parent)

            if not is_found(G, n, towers, v, distance_table):
                build_tree(G, t, n, parent + "," + str(n), distance_table, towers)


def optimal_path(G, target, towers):
    all_path = Tree()
    all_path.create_node(target, str(target))

    distance_table = []
    for t in towers:
        distance_table.append(populate_distance_table(G, t))

    build_tree(G, all_path, target, str(target), distance_table, towers)

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
def find_optimal_node(G, towers):
    path_size = []

    for n in G.nodes():
        if n not in towers:
            opt = optimal_path(G, n, towers)
            path_size.append(opt)

    longest_distance = max(path_size, key=operator.itemgetter(0))[0]

    return_arr = []
    for d in path_size:
        if d[0] == longest_distance:
            return_arr.append(d[1])

    return longest_distance, return_arr
