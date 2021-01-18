# Return an Array of the Possible target Locations
# Parameters:
#   Dictionary of Distance to Every Node from Tower
#   Array of Distance to Target from each Tower
#   Array of Visited Nodes
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
