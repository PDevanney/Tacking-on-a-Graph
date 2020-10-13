import networkx as nx


# Return the distance from a given Tower to the Target
# Parameters:
#   Graph G
#   Tower tower_location
#   Target target_location
# Output:
#   int Distance from Tower to Target node.
def current_distance_to_target(G, tower_location, target_location):
    try:
        return len(nx.dijkstra_path(G, tower_location, target_location))
    except:
        return -1


# Return Array of dict items of the distance from a given Tower to every other node
# Parameters:
#   Graph G
#   int tower_location
# Output:
#   Dict items Distance from Node to Array
def populate_distance_table(G, tower):
    tower_distance = {}
    for node in G.nodes():
        try:
            tower_distance[node] = len(nx.dijkstra_path(G, tower, node))
        except:
            tower_distance[node] = -1
    return tower_distance


# Return a list of indexes for each tower of the possible nodes
# Parameters:
#   Dictionary of Distance to Every Node from Tower
#   Array of Distance to Target from each Tower
# Output:
#   2D Array of Possible Nodes for each Tower
def get_possible_nodes(distance_to_every_node, distance_to_target, visited_nodes):
    possible_nodes = []
    current_tower = 0

    for tower in distance_to_every_node:
        possible_nodes_ind = []
        for node in tower:
            if (tower[node] == distance_to_target[current_tower]) and (node not in visited_nodes):
                possible_nodes_ind.append(node)
        possible_nodes.append(possible_nodes_ind)
        current_tower += 1

    return possible_nodes


# Return an Array of the Possible target Locations
# Parameters:
#   2D Array of Possible Nodes for each Tower
# Output:
#   Array of Intersection of Input Array
def confirmed_node(possible_nodes):
    # Remove Empty Lists from Possible Nodes
    possible_nodes = [x for x in possible_nodes if x != []]

    if len(possible_nodes) == 1:
        return possible_nodes[0]

    setList = []
    for arr in possible_nodes:
        setList.append(set(arr))

    return list(set.intersection(*setList))
