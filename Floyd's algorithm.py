INF = float('inf')  # Representing infinity

def floyd_warshall(graph):
    """
    Args:
        graph: A 2D array representing the graph, where graph[i][j] is the weight of edge (i, j).

    Returns:
        A 2D array representing the shortest distances between all pairs of vertices.
    """

    V = len(graph)
    distances = graph.copy()  # Initialize distance matrix

    # Iterate through all possible intermediate vertices
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]

# Find all-pairs shortest paths
all_pair_shortest_paths = floyd_warshall(graph)

print(all_pair_shortest_paths)
