import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from treelib import *

from search import *


# Need Graph G
# Need the Starting Node
# Distance to other Nodes
def optimal_path_from_start(G, start_node, distance):
    all_paths = Tree()

    all_paths.create_node(1, 1)
    all_paths.show()


def isfound(node, visited):
    # Check if this path will be found.
    pass


G = nx.pappus_graph()
target_node = 1

# Draw Graph
plt.subplot(111)
nx.draw_networkx(G, with_labels=True, font_weight='bold')
plt.show()

all_path = Tree()
all_path.create_node(target_node, str(target_node))


def build_tree(t, node, parent):
    v = [int(n) for n in parent.split(',')]
    for n in G.neighbors(node):
        if n not in v:
            ident = parent + "," + str(n)

            t.create_node(n, ident, parent=parent)

            build_tree(t, n, parent + "," + str(n))


build_tree(all_path, target_node, str(target_node))

all_path.show()
