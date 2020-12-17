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
def search(distance_to_every_node, distance_to_target, visited_nodes):
    current_tower = 0
    possible = []

    for tower in distance_to_every_node:
        possible_nodes_ind = []
        for node in tower:
            if (tower[node] == distance_to_target[current_tower]) and (node not in visited_nodes):
                possible_nodes_ind.append(node)
        possible.append(possible_nodes_ind)
        current_tower += 1

    possible = [x for x in possible if x != []]

    if len(possible) == 0:
        return []
    elif len(possible) == 1:
        return possible[0]
    else:
        setlist = []
        for arr in possible:
            setlist.append(set(arr))

        return list(set.intersection(*setlist))
