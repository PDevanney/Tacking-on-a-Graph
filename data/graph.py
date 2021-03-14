import csv
import matplotlib.pyplot as plt


def read_in_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        output = []
        for row in csv_reader:
            if line_count != 0:
                if row[4] == "Unknown" or row[5] == "Target Location Timeout":
                    pass
                else:
                    output.append(row)
            line_count += 1
    return output


def split_1(input, index):
    d = {}
    for x in input:
        if x[index] in d:
            d[x[index]].append(x)
        else:
            d[x[index]] = [x]
    return d


def split_2(input, index):
    for r in input:
        d = {}
        for x in input[r]:
            if x[index] in d:
                d[x[index]].append(x)
            else:
                d[x[index]] = [x]
        input[r] = d

    return input


def split_3(input, index):
    for r in input:
        for g in input[r]:
            d = {}
            for x in input[r][g]:
                if x[index] in d:
                    d[x[index]].append(x)
                else:
                    d[x[index]] = [x]
            input[r][g] = d
    return input


def split_4(input, index):
    for r in input:
        for g in input[r]:
            for tower in input[r][g]:
                d = {}
                for x in input[r][g][tower]:
                    if x[index] in d:
                        d[x[index]].append(x)
                    else:
                        d[x[index]] = [x]
                input[r][g][tower] = d
    return input


def split_5(input, index):
    for r in input:
        for g in input[r]:
            for tower in input[r][g]:
                for target in input[r][g][tower]:
                    d = {}
                    for x in input[r][g][tower][target]:
                        if x[index] in d:
                            d[x[index]].append(x)
                        else:
                            d[x[index]] = [x]
                    input[r][g][tower][target] = d
    return input


def create_plots(target_type):
    for run in target_type:
        for graph in target_type[run]:
            for tower in target_type[run][graph]:
                f = plt.figure()
                for target in target_type[run][graph][tower]:
                    turn = []
                    size = []
                    for data in target_type[run][graph][tower][target]:
                        # Turn Recordings
                        turn.append(int(data[5]))

                        # Graph Size
                        size.append(int(data[1]))

                    plt.plot(size, turn, label=target[:-6] + " Target", linestyle='--', marker='x')
                plt.xlabel("Graph Size")
                plt.ylabel("Turn Count")

                if graph == "ErdosRenyi":
                    title = tower[:-5] + " Tower on Erdos Renyi"
                else:
                    title = tower[:-5] + " Tower on Random Tree"
                plt.title(title)
                plt.legend()
                f.savefig("graph_output/turn_count/" + run + "_" + title + ".pdf", bbox_inches='tight')
                plt.close(f)

                f = plt.figure()
                for target in target_type[run][graph][tower]:
                    turn = []
                    size = []
                    total_time = []

                    for data in target_type[run][graph][tower][target]:
                        # Clock Time Recordings
                        total_time.append(float(data[6]) + float(data[7]) + float(data[9]))

                        # Graph Size
                        size.append(int(data[1]))

                    plt.plot(size, total_time, label=target[:-6] + " Target", linestyle='--', marker='x')
                plt.xlabel("Graph Size")
                plt.ylabel("Clock Time")

                if graph == "ErdosRenyi":
                    title = tower[:-5] + " Tower on Erdos Renyi"
                else:
                    title = tower[:-5] + " Tower on Random Tree"
                plt.title(title)
                plt.legend()
                f.savefig("graph_output/clock_time/" + run + "_" + title + ".pdf", bbox_inches='tight')
                plt.close(f)


def create_towercountplot(run):
    for r in run:
        f = plt.figure()
        turncount = []
        towercount = []

        for i in run[r]:
            turncount.append(int(i[5]))
            towercount.append(int(i[2]))
        plt.plot(towercount, turncount, linestyle='--', marker='x')
        plt.xlabel("Tower Count")
        plt.ylabel("Turn Count")
        plt.title("Tower Count vs. Turn Count")
        f.savefig("graph_output/tower_vs_turncount/" + r + "_TowerVsTurnCount.pdf", bbox_inches='tight')


def average_towercountplot(tower_count):
    run = split_2(tower_count, 6)
    average_turncount = []
    average_towercount = []

    f= plt.figure()
    for tower in run:
        average_towercount.append(tower)
        total = 0

        for r in run[tower]:
            total += int(run[tower][r][0][5])

        average_turncount.append(total/len(tower_count[tower]))

    plt.plot(average_towercount, average_turncount, linestyle='--', marker='x')
    plt.xlabel("Tower Count")
    plt.ylabel("Turn Count")
    plt.title("Tower Count vs. Average Turn Count")
    f.savefig("graph_output/summary_graphs/tower_vs_turncount/Average_TowerVsTurnCount.pdf", bbox_inches='tight')


def create_summaryplots(input):
    g_type = split_1(input, 0)
    tower_type = split_2(g_type, 3)
    target_type = split_3(tower_type, 4)
    size = split_4(target_type, 1)
    run = split_5(size, 10)

    for g in run:
        for tower in run[g]:
            f = plt.figure()
            for target in run[g][tower]:
                turn = []
                size = []
                for s in run[g][tower][target]:
                    average_turn = []
                    for r in run[g][tower][target][s]:
                        for data in run[g][tower][target][s][r]:
                            # Average Turn Count
                            average_turn.append(int(data[5]))

                    turn.append(sum(average_turn)/len(average_turn))
                    size.append(int(s))

                plt.plot(size, turn, label=target[:-6] + " Target", linestyle='--', marker='x')

            plt.xlabel("Graph Size")
            plt.ylabel("Turn Count")

            if g == "ErdosRenyi":
                title = "Summary " + tower[:-5] + " Tower on Erdos Renyi"
            else:
                title = "Summary " + tower[:-5] + " Tower on Random Tree"
            plt.title(title)
            plt.legend()
            plt.grid(b=None, which='major', axis='both')
            f.savefig("graph_output/summary_graphs/turn_count/" + title + ".pdf", bbox_inches='tight')
            plt.close(f)

            f = plt.figure()
            for target in run[g][tower]:
                time = []
                size = []
                for s in run[g][tower][target]:
                    average_time = []
                    for r in run[g][tower][target][s]:
                        for data in run[g][tower][target][s][r]:
                            # Clock Time Recordings
                            average_time.append(float(data[6]) + float(data[7]) + float(data[9]))
                    time.append(sum(average_time)/len(average_time))
                    size.append(int(s))
                plt.plot(size, time, label=target[:-6] + " Target", linestyle='--', marker='x')
            plt.xlabel("Graph Size")
            plt.ylabel("Clock Time")

            if g == "ErdosRenyi":
                title = "Summary " + tower[:-5] + " Tower on Erdos Renyi"
            else:
                title = "Summary " + tower[:-5] + " Tower on Random Tree"
            plt.title(title)
            plt.legend()
            plt.grid(b=None, which='major', axis='both')
            f.savefig("graph_output/summary_graphs/clock_time/" + title + ".pdf", bbox_inches='tight')
            plt.close(f)

# Get Run Graphs
content = read_in_csv('raw/graph_type.csv')
run = split_1(content, 10)
g_type = split_2(run, 0)
tower_type = split_3(g_type, 3)
target_type = split_4(tower_type, 4)
create_plots(target_type)

# Generate Summary Graphs
g_type = split_1(content, 0)
create_summaryplots(content)

content = read_in_csv('raw/tower.csv')
run = split_1(content, 6)
create_towercountplot(run)

tower_count = split_1(content, 2)
average_towercountplot(tower_count)