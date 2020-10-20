# Optimal Search
# Return an Array of Nodes that are the most likely location of the Target
# Parameters:
#   Graph G
#   int last_target_location
#   Array of Confirmed Nodes
#   int Turn Number
# Output:
#   Array of Nodes
def optimal_possible_nodes(G, last_target_location, confirmed, turn):

    if turn > 0:
        optimal_nodes = []
        neighbours = G.neighbors(last_target_location)

        for n in neighbours:
            if n in confirmed:
                optimal_nodes.append(n)
        return optimal_nodes
    else:
        return confirmed

# Return a list of indexes for each tower of the possible nodes
# Parameters:
#   Dictionary of Distance to Every Node from Tower
#   Array of Distance to Target from each Tower
#   Array of Visited Nodes
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