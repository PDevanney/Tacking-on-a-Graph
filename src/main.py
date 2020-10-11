import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


## ToDo Add Comments ##
## Improve effiency of code ##

def initialise_tracking():
    G = nx.erdos_renyi_graph(20, 0.15)

    tower_count = 3
    target_location = random.randrange(0, G.number_of_nodes())

    tower_location = get_tower_locations(tower_count, G.number_of_nodes(), target_location)
    node_colours = get_node_colours(G.number_of_nodes(), tower_location, target_location)

    #return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    distance_to_every_node = populate_distance_table(G, tower_location)

    #return an array of size m for each Tower
    distance_to_target = current_distance_to_target(G, tower_location, target_location)


#    for tower in range(tower_count):
#        print('Distance to Target from Tower %d : %d' % (tower+1, distance_to_target[tower]))
#        print('Distance to Every node from Tower %d :' % (tower+1))
#        print(distance_to_every_node[tower])
#        print("----------------")

    possible_nodes = get_possible_nodes(distance_to_every_node, distance_to_target)
#    print("Possible nodes : ", possible_nodes)

    confirmed = confirmed_node(possible_nodes)

#    if len(confirmed) == 1:
#        print("The target is at %d" % confirmed[0])
#    else:
#        print("Target unknown")
#        print(confirmed)

    if target_location in confirmed or confirmed == [-1]:
        return 0
    else:
        return 1

    nx.draw_shell(G, with_labels=True, font_weight='bold', node_color=node_colours)

    plt.show()


def get_tower_locations(tower_count, number_of_nodes, target_location):
    tower_location = []
    while len(tower_location) != tower_count:
        position = random.randrange(0, number_of_nodes)
        if position != target_location:
            tower_location.append(position)
    return tower_location

def get_node_colours(number_of_nodes, tower_location, target_location):
    node_colours = []

    target = 'blue'
    tower = 'red'
    unvisited = 'gray'
    visited = 'green'

    for i in range(number_of_nodes):
        if i in tower_location:
            node_colours.append(tower)
        elif i == target_location:
            node_colours.append(target)
        else:
            node_colours.append(visited)

    return node_colours

def current_distance_to_target(G, tower_location, target_location):
    distance = []

    for tower in tower_location:
        try:
            distance.append(len(nx.dijkstra_path(G, tower, target_location)))
        except:
            distance.append(-1)
        finally:
            pass
    return distance

def populate_distance_table(G, tower_location):
    distance = []

    for tower in tower_location:
        tower_distance = {}
        for node in G.nodes():
            try:
                tower_distance[node] = len(nx.dijkstra_path(G, tower, node))
            except:
                tower_distance[node] = -1
            finally:
                pass
        distance.append(tower_distance)
    return distance

# Return a list of indexes for each tower of the possible nodes
def get_possible_nodes(every_node, target):

    nodes = []
    current_tower = 0
    for tower in every_node:
        possible_nodes_indv = []
        for node in range(len(tower)):
            if tower[node] == target[current_tower] and tower[node] != -1:
                possible_nodes_indv.append(node)
        nodes.append(possible_nodes_indv)

        current_tower += 1

    return nodes

def confirmed_node(possible_nodes):
    np_A = np.array(possible_nodes, dtype=object)

    if len(np_A[0]) != 0 and len(np_A[1]) != 0 and len(np_A[2]) != 0:
        return np.intersect1d(np_A[0], np.intersect1d(np_A[1], np_A[2]))
    else:
        return np.intersect1d([-1,-1], np.intersect1d([-1,-1], [-1,-1]))

if __name__ == '__main__':
    for i in range(100):
        yes = initialise_tracking()
        if yes == 1:
            print("NO")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
