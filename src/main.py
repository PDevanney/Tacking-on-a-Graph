import os
import logging
import multiprocessing
import sys
import time
import csv
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from target import *
from tower import *
from playable import *

TIMEOUT = 300
GRAPHSIZE = 40
TOWERCOUNT = 3


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info("Code has started Execution")

    found = False

    if len(sys.argv) == 4:
        if (sys.argv[1]) == "True":
            playable = True
        else:
            playable = False
        graph_size = int(sys.argv[2])
        tower_count = int(sys.argv[3])
    else:
        playable = True
        graph_size = GRAPHSIZE
        tower_count = TOWERCOUNT

    tower_type = [RandomTower(), HeuristicTower(), OptimalTower()]
    target_type = [RandomTarget(), HeuristicTarget(), OptimalTarget()]
    graph_type = ["ErdosRenyi", "Tree"]
    graph_size_array = np.arange(4, 51)
    test_graph_size = [50, 100, 250, 500, 1000]

    # Check if the game mode is Playable (Interactive) or Evaluative
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
        with open('../data/raw/graph_type.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Graph Type", "Graph Size", "Tower Count", "Tower Type", "Target Type", "Turns",
                             "Tower Clock Time", "Target Location Clock Time", "Target Move Clock Time",
                             "Total Time", "Run Number"
                             ])

            for run in range(0, 10):
                logging.info("Run %d has started" % run)
                # Loop through all combinations of the Tower/Target for each Graph Type
                # Loop through each different Graph Type, Graph Size, Tower, and Target combination.
                for g in graph_type:
                    for size in graph_size_array:
                        logging.info("%s of size %d is being processed" % (g, size))
                        turn_list = []

                        if g == "ErdosRenyi":
                            graph = nx.erdos_renyi_graph(size, 0.15)
                        elif g == "Tree":
                            graph = nx.random_tree(size)

                        for tower in tower_type:
                            # Establish initial positioning
                            # With TimeOut Clause

                            starttime = time.asctime()
                            manager = multiprocessing.Manager()
                            tower_location = manager.dict()
                            p = multiprocessing.Process(target=tower.initial_position, name='Tower_Initial_Position',
                                                        args=(graph, tower_count, tower_location))
                            tower_location_start_time = time.time()
                            p.start()
                            p.join(timeout=TIMEOUT)
                            tower_location_finish_time = time.time()
                            p.terminate()

                            if p.exitcode == 0:
                                tower_location = tower_location.values()[0]
                            else:
                                writer.writerow([g, size, tower_count, type(tower).__name__, "Unknown",
                                                 "Tower Initial Position Timeout", "", "", "", "", run])
                                logging.info("%s has timed out" % (type(tower)))

                                file.flush()
                                os.fsync(file.fileno())

                                continue

                            tower_location_elapsed_time = tower_location_finish_time - tower_location_start_time

                            for target in target_type:
                                found = False
                                turn_number = 0
                                visited = []
                                target_movement_elapsed_time = 0

                                total_start_time = time.time()

                                manager = multiprocessing.Manager()
                                target_location = manager.dict()

                                if type(target) == OptimalTarget:
                                    p = multiprocessing.Process(target=target.optimal_path,
                                                                name='Target_Initial_Position',
                                                                args=(graph, tower_location, target_location))

                                    target_location_start_time = time.time()
                                    p.start()
                                    p.join(timeout=TIMEOUT)
                                    target_location_finish_time = time.time()

                                    p.terminate()

                                    if p.exitcode == 0:
                                        longest_path = target_location.values()[0]
                                        target_location = target.initial_location(graph, longest_path)
                                    else:
                                        writer.writerow(
                                            [g, size, tower_count, type(tower).__name__, type(target).__name__,
                                             "Target Location Timeout", "", "", "", "", run])

                                        logging.info("%s has timed out" % type(target))

                                        file.flush()
                                        os.fsync(file.fileno())

                                        continue
                                else:
                                    p = multiprocessing.Process(target=target.initial_location,
                                                                name='Target_Initial_Position',
                                                                args=(graph, tower_location, target_location))

                                    p.start()
                                    target_location_start_time = time.time()
                                    p.join(timeout=TIMEOUT)
                                    target_location_finish_time = time.time()
                                    p.terminate()

                                    if p.exitcode == 0:
                                        target_location = target_location.values()[0]
                                    else:
                                        writer.writerow([g, size, tower_count, type(tower).__name__,
                                                         type(target).__name__,
                                                         "Target Location Timeout", "", "", "", "", run])

                                        logging.info("%s has timed out" % type(target))

                                        file.flush()
                                        os.fsync(file.fileno())

                                        continue

                                target_location_elapsed_time = target_location_finish_time - target_location_start_time

                                # Add towers to visited so that Target cannot go there
                                for t in tower_location:
                                    visited.append(t)

                                distance_to_every_node = []
                                for t in tower_location:
                                    distance_to_every_node.append(populate_distance_table(graph, t))

                                # Each turn
                                while not found:
                                    found = is_found(graph, target_location, tower_location, visited,
                                                     distance_to_every_node)

                                    if not found:
                                        possible_moves = []
                                        for i in graph.neighbors(target_location):
                                            if i not in visited:
                                                possible_moves.append(i)

                                        if len(possible_moves) == 0:
                                            found = True
                                        else:
                                            turn_number += 1
                                            visited.append(target_location)
                                            target_movement_start_time = time.time()
                                            if type(target) == OptimalTarget:
                                                target_location = target.next_move(longest_path, turn_number)
                                            elif type(target) == HeuristicTarget:
                                                target_location = \
                                                    target.heuristic_target_next_move(graph,
                                                                                      tower_location,
                                                                                      visited,
                                                                                      distance_to_every_node,
                                                                                      possible_moves)
                                            else:
                                                target_location = target.next_move(possible_moves, turn_number)

                                            target_movement_finish_time = time.time()

                                            target_movement_elapsed_time = target_movement_elapsed_time + (
                                                    target_movement_finish_time - target_movement_start_time)

                                total_end_time = time.time()
                                total_elapsed_time = total_end_time - total_start_time

                                turn_list.append(turn_number)
                                writer.writerow([g, size, tower_count, type(tower).__name__, type(target).__name__,
                                                 turn_number, tower_location_elapsed_time, target_location_elapsed_time,
                                                 target_movement_elapsed_time, total_elapsed_time, run])

                                file.flush()
                                os.fsync(file.fileno())

            file.flush()
            os.fsync(file.fileno())

        with open("../data/raw/tower.csv", 'w', newline='') as file:
            tower = RandomTower
            target = RandomTarget
            tower_count_array = np.arange(1, 31)
            graph_size = 500
            writer = csv.writer(file)
            writer.writerow(["Graph Type", "Graph Size", "Tower Count", "Tower Type", "Target Type", "Turns",
                             "Run Number"])

            for run in range(0, 10):
                graph = nx.erdos_renyi_graph(graph_size, 0.15)
                logging.info("Tower Run %d has started" % run)
                for count in tower_count_array:
                    logging.info("%d is being evaluated" % count)
                    found = False
                    turn_number = 0
                    visited = []

                    tower_locations = tower.initial_position(graph, count)
                    target_location = target.initial_location(graph, tower_locations)

                    # Add towers to visited so that Target cannot go there
                    for t in tower_locations:
                        visited.append(t)

                    distance_to_every_node = []
                    for t in tower_locations:
                        distance_to_every_node.append(populate_distance_table(graph, t))

                    # Each turn
                    while not found:
                        found = is_found(graph, target_location, tower_locations, visited,
                                         distance_to_every_node)

                        if not found:
                            possible_moves = []
                            for i in graph.neighbors(target_location):
                                if i not in visited:
                                    possible_moves.append(i)

                            if len(possible_moves) == 0:
                                found = True
                            else:
                                turn_number += 1
                                visited.append(target_location)
                                target_location = target.next_move(possible_moves, turn_number)

                    logging.info("Node found in %d turns" % turn_number)
                    writer.writerow(["Erdos Renyi", graph_size, count, type(tower).__name__, type(target).__name__,
                                     turn_number, run])

                    file.flush()
                    os.fsync(file.fileno())

            file.flush()
            os.fsync(file.fileno())
