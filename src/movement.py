import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from treelib import *

from src.distances import *
from src.search import *



def isfound(node, visited):
    # Check if this path will be found.
    return False


G = nx.pappus_graph()
target_node = 1
towers = [0]

distance_table = populate_distance_table(G, 0)
current_distance_to_target(G, 0, target_node)
#get_possible_nodes()

# Draw Graph
plt.subplot(111)
nx.draw_networkx(G, with_labels=True, font_weight='bold')
plt.show()

all_path = Tree()
all_path.create_node(target_node, str(target_node))


def build_tree(t, node, parent):
    v = [int(n) for n in parent.split(',')]
    v = v + towers
    for n in G.neighbors(node):
        if n not in v:
            ident = parent + "," + str(n)

            t.create_node(n, ident, parent=parent)

            if not isfound(n, v):
                build_tree(t, n, parent + "," + str(n))


build_tree(all_path, target_node, str(target_node))

all_path.show()

leaves = all_path.leaves()

print(leaves)
