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
        return len(nx.dijkstra_path(G, tower_location, target_location)) - 1
    except nx.NetworkXNoPath:
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
            tower_distance[node] = len(nx.dijkstra_path(G, tower, node)) - 1
        except nx.NetworkXNoPath:
            tower_distance[node] = -1
    return tower_distance
