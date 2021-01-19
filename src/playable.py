import matplotlib.pyplot as plt
import networkx as nx

from src.movement import is_found


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


def get_node_colours(number_of_nodes, tower_location, target_location, visited,
                     target_colour='blue', tower_colour='red', unvisited_colour='gray', visited_colour= 'green'):

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
