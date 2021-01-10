import matplotlib.pyplot as plt
import networkx as nx
import time
from tabulate import tabulate

from distances import *
from search import *
from target import *
from tower import *


def tracking(target_location, tower_location, visited, node_pos, distance):
    # Set node colours for the graph
    node_colours = get_node_colours(graph_size, tower_location, target_location, visited_nodes)

    distance_to_target = []
    for tower in tower_location:
        distance_to_target.append(current_distance_to_target(G, tower, target_location))

    # return an Array of Dictionary items. Each dictionary is node_name:distance for each tower
    confirmed = search(distance, distance_to_target, visited)

    # Draw Graph
    plt.subplot(111)
    nx.draw_networkx(G, with_labels=True, font_weight='bold', node_color=node_colours, pos=node_pos)
    plt.show()

    return len(confirmed) == 1


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


# def driver(graph_type, graph_size, tower_count=3,
#           tower_pos="random", target_pos="random",
#           tower_search="normal", target_movement="random"):
#    graph_types = {"complete" + str(graph_size): nx.complete_graph(graph_size),
#                   "erdos" + str(graph_size): nx.erdos_renyi_graph(graph_size, 0.15)
#                   }
#
#    graph = graph_types[graph_type + str(graph_size)]
#
#    # Establish initial positioning
#    location_start_time = time.time()
#
#    #
#
#    location_finish_time = time.time()
#    location_elapsed_time = location_finish_time - location_start_time
#
#    # movement / searching
#    # play the game
#    plt.subplot(111)
#    nx.draw_networkx(graph, with_labels=True, font_weight='bold')
#    plt.show()
#
#    print("Time for Location: ", location_elapsed_time, end="")
#    print(" Using Tower - ", tower_pos, " Target - ", target_pos)
#    print(tabulate([
#        ['Tower Position', tower_pos, location_elapsed_time],
#        ['Target Position', target_pos, location_elapsed_time],
#
#        ['Tower Searching', tower_pos, location_elapsed_time, 7],
#        ['Target Movement', target_pos, location_elapsed_time, 5]
#
#    ], headers=['', 'Type', 'Time', 'Turns']))


# ToDo Fix Bug for a node with no possible movements (Disconnected graph)
if __name__ == '__main__':
    found = False
    playable = False
    graph_size = 18
    tower_count = 3

    tower_type = [RandomTower(), HeuristicTower(), OptimalTower()]
    target_type = [RandomTarget(), HeuristicTarget(), OptimalTarget()]

    # Create the initial graph
    # G = nx.erdos_renyi_graph(graph_size, 0.15)
    G = nx.pappus_graph()

    # Loop through all combinations of the Tower/Target
    for tower in tower_type:
        for target in target_type:

            print("Target -- ", type(tower).__name__)
            print("Tower -- ", type(target).__name__)

            found = False
            playable = False
            turn_number = 0
            visited_nodes = []

            # Define the initial position of the Tower/Target
            tower_location = tower.initial_position(G, tower_count)
            print("Initial Tower Location -- ", tower_location)

            # ToDo Logic of this section
            if type(target) == OptimalTarget:
                print("tower -- ", tower_location)
                longest_path = find_optimal_node(G, tower_location)[1][0]
                print("lp -- ", longest_path)

                longest_path = list(map(int, longest_path))
                target_location = target.initial_location(G, longest_path)
            else:
                target_location = target.initial_location(G, tower_location)

            print("Initial Target Location -- ", target_location)

            # Add towers to visited so that Target cannot go there
            for t in tower_location:
                visited_nodes.append(t)

            # Position the Nodes so they do not change each turn
            node_positions = nx.fruchterman_reingold_layout(G, seed=42)

            distance_to_every_node = []
            for location in tower_location:
                distance_to_every_node.append(populate_distance_table(G, location))

            # Each turn
            while not found:
                found = tracking(target_location, tower_location, visited_nodes, node_positions, distance_to_every_node)

                if not found:
                    visited_nodes.append(target_location)
                    possible_moves = []
                    for i in G.neighbors(target_location):
                        if i not in visited_nodes:
                            possible_moves.append(i)

                    if len(possible_moves) == 0:
                        print("No Moves Available")
                        found = True
                        playable = False

                    if playable:
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
                    else:

                        if type(target) == OptimalTarget:
                            turn_number += 1
                            target_location = target.next_move(longest_path, turn_number)
                        else:
                            turn_number += 1
                            target_location = target.next_move(possible_moves, turn_number)

            print("Target found in %d turns" % turn_number)
            print("Target visited ", end='')
            for t in visited_nodes[3:]:
                print("%d -> " % t, end='')
            print(target_location)
