import csv
from pprint import pprint

import matplotlib.pyplot as plt

# Create Graphs for Target vs. Tower Evaluation
with open('output/graph_type.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    output = {
        "ErdosRenyi":
            {
                "RandomTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []},
                "HeuristicTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []},
                "OptimalTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []}
            },
        "Tree":
            {
                "RandomTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []},
                "HeuristicTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []},
                "OptimalTower": {"RandomTarget": [], "HeuristicTarget": [], "OptimalTarget": []}
            }
    }

    for row in csv_reader:
        if line_count != 0:
            if row[4] == "Unknown":
                pass
            else:
                output[row[0]][row[3]][row[4]].append(row)
        line_count += 1

for graph_type in output:
    for tower_type in output[graph_type]:
        f = plt.figure()
        for target_type in output[graph_type][tower_type]:
            turn = []
            size = []
            tower_location = []
            target_location = []
            target_move = []

            for data in output[graph_type][tower_type][target_type]:
                # Turn Recordings
                if data[5] == "Target Location Timeout":
                    pass
                else:
                    turn.append(int(data[5]))

                    # Clock Time Recordings
                    tower_location.append(float(data[6]))
                    target_location.append(float(data[7]))
                    target_move.append(float(data[8]))

                    size.append(int(data[1]))

            plt.plot(size, turn, label=target_type[:-6] + " Target", linestyle='--', marker='x')
        plt.xlabel("Graph Size")
        plt.ylabel("Turn Count")

        if graph_type == "ErdosRenyi":
            title = tower_type[:-5] + " Tower on Erdos Renyi"
        else:
            title = tower_type[:-5] + " Tower on Random Tree"
        plt.title(title)
        plt.legend()
        plt.show()
        f.savefig("graph_output/" + title + ".pdf", bbox_inches='tight')

# Create graph_output for Tower Count Evaluation
with open('output/tower.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    graph_data = []

    tower = []
    turn = []
    for row in csv_reader:
        if line_count != 0:
            tower.append(row[2])
            turn.append(int(row[5]))

        line_count += 1

    f = plt.figure()
    plt.plot(tower, turn, linestyle='--', marker='x')
    plt.xlabel("Tower Count")
    plt.ylabel("Turn Count")
    plt.title("Tower Count vs. Turn Count")
    plt.show()
    f.savefig("graph_output/TowerVsTurnCount.pdf", bbox_inches='tight')