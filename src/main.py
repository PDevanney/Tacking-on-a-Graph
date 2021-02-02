import sys
import time
import csv
import matplotlib.pyplot as plt
import networkx as nx
from target import *
from tower import *
from playable import *


if __name__ == '__main__':
    output = open('output.csv', 'a', newline='')
    writer = csv.writer(output)
    writer.writerow(["Graph Type", "Graph Size", "Tower Count", "RTo RTa", "RTo HTa", "RTo OTa", "HTo RTa", "HTo HTa",
                     "HTo OTa", "OTo RTa", "OTo HTa", "OTo OTa"])

    found = False

    if len(sys.argv) == 4:
        if (sys.argv[1]) == "True":
            playable = True
        else:
            playable = False
        graph_size = int(sys.argv[2])
        tower_count = int(sys.argv[3])
    else:
        playable = False
        graph_size = 50
        tower_count = 10

    #tower_type = [RandomTower(), HeuristicTower(), OptimalTower()]
    #target_type = [RandomTarget(), HeuristicTarget(), OptimalTarget()]
    tower_type = [RandomTower(), HeuristicTower()]
    target_type = [RandomTarget(), HeuristicTarget()]

    graph_type = [nx.erdos_renyi_graph(graph_size, 0.15), nx.random_tree(graph_size)]

    if playable:
        print("Playable Method")
        print("-----------------")
        print("\n")

        graph = nx.erdos_renyi_graph(graph_size, 0.15)
        turn_number = 0
        visited = []

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

        while not found:
            found = tracking(graph, target_location, tower_location, visited, node_positions, distance_to_every_node)

            if not found:
                possible_moves = []
                print("Possible Moves: ", end='')
                for i in graph.neighbors(target_location):
                    if i not in visited:
                        print(i, end=" ")
                        possible_moves.append(i)

                if len(possible_moves) == 0:
                    print("No Moves Available!")
                    found = True
                else:
                    print()
                    visited.append(target_location)
                    value = input("Please enter a Node to move to from the above Possible Moves?\n")

                    if value == 'n':
                        for neighbour in possible_moves:
                            print(neighbour, end=' ')
                        print("")
                        value = input("Please enter a Node to move to from the above Possible Moves?\n")
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

        # Loop through all combinations of the Tower/Target for each Graph Type
        for graph in graph_type:
            turn_list = []
            for tower in tower_type:
                for target in target_type:
                    print("Target: ", type(tower).__name__)
                    print("Tower: ", type(target).__name__)

                    found = False
                    turn_number = 0
                    visited = []
                    target_movement_elapsed_time = 0
                    total_start_time = time.time()

                    # Establish initial positioning
                    tower_location_start_time = time.time()
                    tower_location = tower.initial_position(graph, tower_count)
                    tower_location_finish_time = time.time()

                    tower_location_elapsed_time = tower_location_finish_time - tower_location_start_time
                    print("Initial Tower Location: ", tower_location)

                    target_location_start_time = time.time()
                    if type(target) == OptimalTarget:
                        longest_path = find_optimal_node(graph, tower_location)[1][0]
                        longest_path = list(map(int, longest_path))

                        target_location = target.initial_location(graph, longest_path)
                    else:
                        target_location = target.initial_location(graph, tower_location)

                    target_location_finish_time = time.time()
                    target_location_elapsed_time = target_location_finish_time - target_location_start_time

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
                                target_movement_start_time = time.time()
                                if type(target) == OptimalTarget:
                                    target_location = target.next_move(longest_path, turn_number)
                                elif type(target) == HeuristicTarget:
                                    target_location = target.heuristic_target_next_move(graph, tower_location, visited,
                                                                                        distance_to_every_node, possible_moves)
                                else:
                                    target_location = target.next_move(possible_moves, turn_number)
                                target_movement_finish_time = time.time()

                                target_movement_elapsed_time = target_movement_elapsed_time + \
                                                               (target_movement_finish_time - target_movement_start_time)

                        else:
                            print("Found!")

                    total_end_time = time.time()
                    total_elapsed_time = total_end_time - total_start_time

                    turn_list.append(turn_number)
                    print("Target found in %d turns" % turn_number)
                    print("Tower Location : ", tower_location_elapsed_time, end='')
                    print("\tTarget Location : ", target_location_elapsed_time)
                    print("Target Movement : ", target_movement_elapsed_time)
                    print("Total Time : ", total_elapsed_time)

                    print("Target visited ", end='')
                    for t in visited[tower_count:]:
                        print("%d -> " % t, end='')
                    print(target_location)
                    print("\n")

            info = ["Graph Type", graph_size, tower_count]
            writer.writerow(info + turn_list)

