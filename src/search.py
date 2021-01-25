# Return a List of the Possible Locations of the Target on the Graph
# Parameters:
#   A dictionary of Distance to Every Node from Tower keyed by Node
#   List[int] Distance to Target from each Tower
#   List[int] Previously Visited Nodes
# Output:
#   List[int] possible locations (Intersection of Input Array)
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
