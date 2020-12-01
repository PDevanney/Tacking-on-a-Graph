import operator
from treelib import *

from src.distances import *
from src.driver import search_driver


def isfound(graph, target, tower, visited, distances):
    s = search_driver(graph, target, tower, visited, distances)

    if len(s) == 1:
        return True
    return False


def build_tree(G, t, node, parent, distance_table, towers):
    pass
    v = [int(n) for n in parent.split(',')]
    v = v + towers
    for n in G.neighbors(node):
        if n not in v:
            ident = parent + "," + str(n)

            t.create_node(n, ident, parent=parent)

            if not isfound(G, n, towers, v, distance_table):
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
    for l in leaves:
        depth[l.identifier] = all_path.depth(l)

    longest_path_string = max(depth.items(), key=operator.itemgetter(1))[0]
    longest_path = longest_path_string.split(',')

    return len(longest_path), longest_path


def find_optimal_node(G, towers):
    path_size = []

    for n in G.nodes():
        if n not in towers:
            opt = optimal_path(G, n, towers)
            print(n, ": ", opt)
            path_size.append(opt)

    longest_distance = max(path_size)[0]

    return_arr = []
    for d in path_size:
        if d[0] == longest_distance:
            return_arr.append(d[1])

    return return_arr


print(find_optimal_node(nx.pappus_graph(), [0, 2, 3]))

# Adapt optimal_path to return every path not just one.
# Adapt overs to fit this schematic
# Adapt tracking() to use search driver function
