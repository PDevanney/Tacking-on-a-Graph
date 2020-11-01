import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from treelib import Tree, Node

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
all_path.create_node("Root", [target_node])
for n in G.neighbors(target_node):
    all_path.create_node([n]+[target_node], [n]+[target_node], parent=target_node)

    for i in G.neighbors(n):
        all_path.create_node(i, i, parent=n)

all_path.show()
