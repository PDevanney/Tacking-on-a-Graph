import networkx as nx


# Return the distance from a given Tower to the Target
# Parameters:
#   Graph graph
#   int tower_location
#   int target_location
# Output:
#   int Distance from Tower to Target node.
def current_distance_to_target(graph, tower_location, target_location):
    try:
        return len(nx.dijkstra_path(graph, tower_location, target_location)) - 1
    except nx.NetworkXNoPath:
        return -1


# Return a dictionary of the distance from a given Tower to every other node keyed by Graph Node
# Parameters:
#   Graph graph
#   int tower_location
# Output:
#   A dictionary of distances keyed by Node
def populate_distance_table(graph, tower_location):
    tower_distance = {}
    for node in graph.nodes():
        try:
            tower_distance[node] = len(nx.dijkstra_path(graph, tower_location, node)) - 1
        except nx.NetworkXNoPath:
            tower_distance[node] = -1
    return tower_distance
