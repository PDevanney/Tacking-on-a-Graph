import time
import gc
import matplotlib.pyplot as plt
import networkx as nx

from distances import *
from search import *
from target import *
from tower import *
from playable import *

print("Tracking Test")
print("--------------/n")

tower = RandomTower()
tower_count = 3
target = OptimalTarget()


for i in range(tower_count+1, 101):
    graph = nx.erdos_renyi_graph(i, 0.15, seed=50)
    tower_location = tower.initial_position(graph, tower_count)
    target_location_start_time = time.time()

    longest_path = find_optimal_node(graph, tower_location)[1][0]
    longest_path = list(map(int, longest_path))
    target_location = target.initial_location(graph, longest_path)

    target_location_finish_time = time.time()
    target_location_elapsed_time = target_location_finish_time - target_location_start_time

    if target_location_elapsed_time > 20:
        plt.subplot(111)
        nx.draw_networkx(graph, with_labels=True, font_weight='bold')
        plt.show()

    print(i, target_location_elapsed_time)

    gc.collect()
