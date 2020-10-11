import random
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from functools import reduce


## ToDo Add Comments ##
def tracking(tower_count, target_location, tower_location, turn_number):

    # Set node colours for the graph
    node_colours = get_node_colours(graph_size, tower_location, target_location)

    #return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    distance_to_every_node = populate_distance_table(G, tower_location)

    #return an array of size m for each Tower
    distance_to_target = current_distance_to_target(G, tower_location, target_location)

    #print("This is Turn %d" % turn_number, end="\n\n\n")

    #for tower in range(tower_count):
    #    print('Distance to Target from Tower %d at Position %d: %d' % (tower+1, tower_location[tower], distance_to_target[tower]))
    #    print('Distance to Every node from Tower %d :' % (tower+1))
    #    print(distance_to_every_node[tower])
    #    print("----------------")

    possible_nodes = get_possible_nodes(distance_to_every_node, distance_to_target)

    for n in range(tower_count):
        print("Possible nodes from tower %d: " % n, possible_nodes)

    plt.subplot(111)

    nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color=node_colours)

    plt.show()

    confirmed = confirmed_node(possible_nodes)

    if len(confirmed) == 1:
        print("The target is at %d" % confirmed[0])
        return True
    else:
        print("Target unknown ", confirmed)
        return False


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
        elif i in visited_nodes:
            node_colours.append(visited)
        else:
            node_colours.append(unvisited)

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
def get_possible_nodes(distance_to_every_node, distance_to_target):
    possible_nodes = []
    current_tower = 0

    #for each tower go through the distances to every node
    #for each distance check if it hasn't already been visited.

    #possible nodes == correct distance + haven't been visited

    for tower in distance_to_every_node:
        possible_nodes_indv = []
        for node in tower:
            if tower[node] == distance_to_target[current_tower] and tower[node] not in visited_nodes:
                possible_nodes_indv.append(node)
        possible_nodes.append(possible_nodes_indv)
        current_tower += 1

    return possible_nodes

# ToDo Improve Function -- Applicable with More/Less Towers
def confirmed_node(possible_nodes):
    T1 = possible_nodes[0]
    T2 = possible_nodes[1]
    T3 = possible_nodes[2]

    if len(T1) > 0 and len(T2) > 0:
        TT = np.intersect1d(np.array(T1), np.array(T2))
    elif len(T1) == 0:
        TT = T2
    else:
        TT = T1

    if len(TT) > 0 and len(T3) > 0:
        return(np.intersect1d(np.array(TT), np.array(T3)))
    elif len(TT) == 0:
        return(T3)
    else:
        return(TT)

if __name__ == '__main__':
    found = False
    graph_size = 30
    tower_count = 3
    turn_number = 0
    visited_nodes = []

    # create the initial graph
    # populate the initial target location with a random location
    # place the 3 towers
    G = nx.erdos_renyi_graph(graph_size, 0.15)
    target_location = random.randrange(0, graph_size)
    tower_location = get_tower_locations(tower_count, graph_size, target_location)

    # Add towers to visited so that Target cannot go there
    for tower in tower_location:
        visited_nodes.append(tower)

    # Each turn
    while not found:

        found = tracking(tower_count, target_location, tower_location, turn_number)

        if not found:
            visited_nodes.append(target_location)
            for i in G.neighbors(target_location):
                if i not in visited_nodes:
                    print(i, end=" ")

            value = input("Please enter a Node to move to from the above?\n")

            if value == 'n':
                for neighbour in G.neighbors(target_location):
                    print(neighbour, end='')
            else:
                while int(value) not in G.neighbors(target_location) or int(value) in visited_nodes:
                    value = input("Please enter a valid Node to move to from the above?\n")

                target_location = int(value)

            turn_number += 1

    print("Target found in %d turns" % turn_number)
    print("Target visited ", end='')
    for t in visited_nodes[3:]:
        print("%d -> " % t, end='')
    print(target_location)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
