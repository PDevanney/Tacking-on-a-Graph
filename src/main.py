import matplotlib.pyplot as plt
import networkx as nx
import time
from tabulate import tabulate

from src.distances import *
from src.driver import search_driver
from src.search import *
from src.initial_locations import *


def tracking(tower_count, target_location, last_target_location, tower_location, visited_nodes, node_pos):
    # Set node colours for the graph
    node_colours = get_node_colours(graph_size, tower_location, target_location)

    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower

    distance_to_every_node = []
    for location in tower_location:
        distance_to_every_node.append(populate_distance_table(G, location))

    confirmed = search_driver(G, target_location, tower_location, visited_nodes, distance_to_every_node)

    # Draw Graph
    plt.subplot(111)
    nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color=node_colours, pos=node_pos)
    plt.show()

    print('Optimal Search: ', optimal_possible_nodes(G, last_target_location, confirmed, turn_number))

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


def driver(graph_type, graph_size, tower_count=3,
           tower_pos="random", target_pos="random",
           tower_search="normal", target_movement="random"):

    graph_types = {"complete" + str(graph_size): nx.complete_graph(graph_size),
                   "erdos" + str(graph_size): nx.erdos_renyi_graph(graph_size, 0.15)
                   }

    graph = graph_types[graph_type + str(graph_size)]

    # Establish initial positioning
    location_start_time = time.time()

    #

    location_finish_time = time.time()
    location_elapsed_time = location_finish_time - location_start_time

    # movement / searching
    # play the game
    plt.subplot(111)
    nx.draw_networkx(graph, with_labels=True, font_weight='bold')
    plt.show()

    print("Time for Location: ", location_elapsed_time, end="")
    print(" Using Tower - ", tower_pos, " Target - ", target_pos)
    print(tabulate([
        ['Tower Position', tower_pos, location_elapsed_time],
        ['Target Position', target_pos, location_elapsed_time],

        ['Tower Searching', tower_pos, location_elapsed_time, 7],
        ['Target Movement', target_pos, location_elapsed_time, 5]

    ], headers=['', 'Type', 'Time', 'Turns']))

    # Return loc_pos,
    return


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

    # tower_location = get_tower_locations(tower_count, graph_size, target_location)
    tower_location = heuristic_tower_location(G, tower_count)
    target_location = random_target_location(graph_size, tower_location)
    last_target_location = target_location

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
