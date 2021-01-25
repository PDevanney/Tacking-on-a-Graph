import matplotlib.pyplot as plt
import networkx as nx
from distances import *
from search import *


# Return a Boolean value indicating if the Target has been found
# Parameters:
#   Graph graph
#   int target_location
#   List[int] tower_locations
#   List[int] visited
#   A List of dictionary distances keyed by Node: distances
# Output:
#   Boolean is target found
def is_found(graph, target_location, tower_locations, visited, distances):
    distance_to_target = []
    for t in tower_locations:
        distance_to_target.append(current_distance_to_target(graph, t, target_location))

    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    s = search(distances, distance_to_target, visited)
    return len(s) == 1


# Return if target is found, draw appropriate graph.
# Parameters:
#   Graph graph
#   int target_location
#   List[int] tower_location
#   List[int] visited
#   A dictionary of positions keyed by node: node_pos
#   A List of dictionary distances keyed by Node: distances
# Output:
#   Boolean is target found
def tracking(graph, target_location, tower_location, visited, node_pos, distance):
    # Set node colours for the graph
    node_colours = get_node_colours(graph.number_of_nodes(), tower_location, target_location, visited)

    # Check if Target is found
    confirmed = is_found(graph, target_location, tower_location, visited, distance)

    # Draw Graph
    plt.subplot(111)
    nx.draw_networkx(graph, with_labels=True, font_weight='bold', node_color=node_colours, pos=node_pos)
    plt.show()

    return confirmed


# Return List of colours for the Graph.
# Parameters:
#   int number_of_nodes
#   List[int] tower_location
#   int target_location
#   List[int] visited
# Output:
#   List[string] node_colours
def get_node_colours(number_of_nodes, tower_location, target_location, visited):
    target_colour = 'blue'
    tower_colour = 'red'
    unvisited_colour = 'gray'
    visited_colour = 'green'

    node_colours = []

    for node in range(number_of_nodes):
        if node in tower_location:
            node_colours.append(tower_colour)
        elif node == target_location:
            node_colours.append(target_colour)
        elif node in visited:
            node_colours.append(visited_colour)
        else:
            node_colours.append(unvisited_colour)

    return node_colours
