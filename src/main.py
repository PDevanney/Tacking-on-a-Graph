import matplotlib.pyplot as plt

from distances import *
from search import *
from initial_locations import *


def tracking(tower_count, target_location, last_target_location, tower_location, visited_nodes, node_pos):
    # Set node colours for the graph
    node_colours = get_node_colours(graph_size, tower_location, target_location)

    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower

    distance_to_target = []
    distance_to_every_node = []
    for t in tower_location:
        distance_to_every_node.append(populate_distance_table(G, t))
        distance_to_target.append(current_distance_to_target(G, t, target_location))

    possible_nodes = get_possible_nodes(distance_to_every_node, distance_to_target, visited_nodes)

    for n in range(tower_count):
        print("Possible nodes from tower %d: " % n, possible_nodes)

    # Draw Graph
    plt.subplot(111)
    nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color=node_colours, pos=node_pos)
    plt.show()

    confirmed = confirmed_node(possible_nodes)

    optimal = optimal_possible_nodes(G, last_target_location, confirmed, turn_number)
    print(optimal)

    if len(confirmed) == 1:
        print("The target is at %d" % confirmed[0])
        return True
    else:
        print("Target unknown ", confirmed)
        return False


def get_node_colours(number_of_nodes, tower_location, target_location):
    node_colours = []

    target_colour = 'blue'
    tower_colour = 'red'
    unvisited_colour = 'gray'
    visited_colour = 'green'

    for i in range(number_of_nodes):
        if i in tower_location:
            node_colours.append(tower_colour)
        elif i == target_location:
            node_colours.append(target_colour)
        elif i in visited_nodes:
            node_colours.append(visited_colour)
        else:
            node_colours.append(unvisited_colour)

    return node_colours


if __name__ == '__main__':
    found = False
    graph_size = 50
    tower_count = 3
    turn_number = 0
    visited_nodes = []

    # create the initial graph
    # populate the initial target location with a random location
    # place the 3 towers
    G = nx.erdos_renyi_graph(graph_size, 0.15)
    target_location = get_target_location(graph_size)
    last_target_location = target_location

    # tower_location = get_tower_locations(tower_count, graph_size, target_location)
    tower_location = get_optimal_tower_locations(G, tower_count, target_location)

    # Add towers to visited so that Target cannot go there
    for tower in tower_location:
        visited_nodes.append(tower)

    # Position the Nodes so they do not change each turn
    node_positions = nx.fruchterman_reingold_layout(G, seed=42)

    # Each turn
    while not found:
        print("Current Node: ", target_location)
        print("Last Node: ", last_target_location)
        found = tracking(tower_count, target_location, last_target_location,
                         tower_location, visited_nodes, node_positions)

        if not found:
            visited_nodes.append(target_location)
            last_target_location = target_location

            possible_moves = []
            print("Possible Moves : ", end="")
            for i in G.neighbors(target_location):
                if i not in visited_nodes:
                    print(i, end=" ")
                    possible_moves.append(i)

            if len(possible_moves) == 0:
                print("No more valid moves\n"
                      "Game End")
                quit()

            print("")
            value = input("Please enter a Node to move to from the above Possible Moves?")

            if value == 'n':
                for neighbour in possible_moves:
                    print(neighbour, end=' ')
                print("")
            elif value == 'o':
                # optimal = get_optimal_move()
                optimal = possible_moves[0]
                print("The Optimal Move is ", optimal)
                target_location = optimal
            else:
                try:
                    while int(value) not in G.neighbors(target_location) or int(value) in visited_nodes:
                        value = input("Please enter a valid Node to move to from the above?\n")
                except ValueError:
                    print("Invalid Value entered")
                    value = possible_moves[0]
                target_location = int(value)

            turn_number += 1
            print("---------------------------")

    print("Target found in %d turns" % turn_number)
    print("Target visited ", end='')
    for t in visited_nodes[3:]:
        print("%d -> " % t, end='')
    print(target_location)
