import operator
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from treelib import *

from src.distances import *
from src.driver import search_driver


def isfound(graph, target, tower, visited, distances):
    s = search_driver(graph, target, tower, visited, distances)

    if len(s) == 1:
        return True
    return False


G = nx.pappus_graph()
target_node = 1
towers = [0, 2, 3]

distance_table = []
for t in towers:
    distance_table.append(populate_distance_table(G, t))

# Draw Graph
plt.subplot(111)
nx.draw_networkx(G, with_labels=True, font_weight='bold')
plt.show()

all_path = Tree()
all_path.create_node(target_node, str(target_node))


def build_tree(t, node, parent):
    pass
    v = [int(n) for n in parent.split(',')]
    v = v + towers
    for n in G.neighbors(node):
        if n not in v:
            ident = parent + "," + str(n)

            t.create_node(n, ident, parent=parent)

            if not isfound(G, n, towers, v, distance_table):
                build_tree(t, n, parent + "," + str(n))


def optimal_path():

    build_tree(all_path, target_node, str(target_node))
    leaves = all_path.leaves()
    depth = {}
    for l in leaves:
        depth[l.identifier] = all_path.depth(l)

    print(depth)
    longest_path = max(depth.items(), key=operator.itemgetter(1))[0]

    print(longest_path.split(','))

    return 0


optimal_path()
