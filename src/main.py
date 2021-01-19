import matplotlib.pyplot as plt
import networkx as nx

from distances import *
from search import *
from target import *
from tower import *
from playable import *

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
    playable = True
    graph_size = 30
    tower_count = 2

    tower_type = [RandomTower(), HeuristicTower(), OptimalTower()]
    target_type = [RandomTarget(), HeuristicTarget(), OptimalTarget()]

    #    graph_types = {"complete" + str(graph_size): nx.complete_graph(graph_size),
    #                   "erdos" + str(graph_size): nx.erdos_renyi_graph(graph_size, 0.15)
    #                   }
    #
    #    graph = graph_types[graph_type + str(graph_size)]

    # Create the initial graph
    graph = nx.erdos_renyi_graph(graph_size, 0.15)

    if playable:
        print("Playable Method")
        print("-----------------")
        print("\n")

        turn_number = 0
        visited = []

        # ToDo Easy, Medium. Hard Towers
        tower = RandomTower()
        tower_location = tower.initial_position(graph, tower_count)

        node_colours = get_node_colours(graph.number_of_nodes(), tower_location, -1, visited)
        plt.subplot(111)
        nx.draw_networkx(graph, with_labels=True, font_weight='bold', node_color=node_colours)
        plt.show()

        target_location = int(input("Please enter where you wish to begin?\n"))

        for t in tower_location:
            visited.append(t)

        # Position the Nodes so they do not change each turn
        node_positions = nx.fruchterman_reingold_layout(graph, seed=42)

        distance_to_every_node = []
        for location in tower_location:
            distance_to_every_node.append(populate_distance_table(graph, location))

        # ToDo Add Optimal Path

        while not found:
            found = tracking(graph, target_location, tower_location, visited, node_positions, distance_to_every_node)

            if not found:
                possible_moves = []
                for i in graph.neighbors(target_location):
                    if i not in visited:
                        possible_moves.append(i)

                if len(possible_moves) == 0:
                    print("No Moves Available!")
                    found = True
                else:
                    visited.append(target_location)
                    value = input("Please enter a Node to move to from the above Possible Moves?\n")

                    if value == 'n':
                        for neighbour in possible_moves:
                            print(neighbour, end=' ')
                        print("")
                        value = input("Please enter a Node to move to from the above Possible Moves?\n")
                    elif value == 'o':
                        optimal = possible_moves[0]
                        print("The Optimal Move is ", optimal)
                    else:
                        try:
                            while int(value) not in possible_moves:
                                value = input("Please enter a valid Node to move to from the above?\n")
                        except ValueError:
                            print("Invalid Value entered\n")
                            value = possible_moves[0]

                    target_location = int(value)
                    turn_number += 1
            else:
                print("Found!")

        print("Target found in %d turns" % turn_number)
        print("Target visited ", end='')
        for t in visited[tower_count:]:
            print("%d -> " % t, end='')
        print(target_location)
        print("\n")

    else:
        print("Evaluative Method")
        print("-----------------\n")

        # Loop through all combinations of the Tower/Target
        for tower in tower_type:
            for target in target_type:
                print("Target: ", type(tower).__name__)
                print("Tower: ", type(target).__name__)

                found = False
                turn_number = 0
                visited = []

                # Define the initial position of the Tower/Target
                tower_location = tower.initial_position(graph, tower_count)
                print("Initial Tower Location: ", tower_location)

                if type(target) == OptimalTarget:
                    longest_path = find_optimal_node(graph, tower_location)[1][0]
                    longest_path = list(map(int, longest_path))

                    target_location = target.initial_location(graph, longest_path)
                else:
                    target_location = target.initial_location(graph, tower_location)

                print("Initial Target Location: ", target_location)

                # Add towers to visited so that Target cannot go there
                for t in tower_location:
                    visited.append(t)

                distance_to_every_node = []
                for t in tower_location:
                    distance_to_every_node.append(populate_distance_table(graph, t))

                # Each turn
                while not found:
                    found = is_found(graph, target_location, tower_location, visited, distance_to_every_node)

                    if not found:
                        possible_moves = []
                        for i in graph.neighbors(target_location):
                            if i not in visited:
                                possible_moves.append(i)

                        if len(possible_moves) == 0:
                            print("No Moves Available!")
                            found = True
                        else:
                            turn_number += 1
                            visited.append(target_location)
                            if type(target) == OptimalTarget:
                                target_location = target.next_move(longest_path, turn_number)
                            elif type(target) == HeuristicTarget:
                                target_location = target.heuristic_target_next_move(graph, tower_location, visited,
                                                                                    distance_to_every_node, possible_moves)
                            else:
                                target_location = target.next_move(possible_moves, turn_number)
                    else:
                        print("Found!")

                print("Target found in %d turns" % turn_number)
                print("Target visited ", end='')
                for t in visited[tower_count:]:
                    print("%d -> " % t, end='')
                print(target_location)
                print("\n")
