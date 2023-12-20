INF = float('inf')

def floyd_warshall(graph):
    num_nodes = len(graph)
    
    # Initialize the distance matrix
    distance = [[INF] * num_nodes for _ in range(num_nodes)]

    # Initialize distances for existing edges
    for i in range(num_nodes):
        for j, weight in graph[i]:
            distance[i][j] = weight

    # Floyd-Warshall algorithm
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Example usage:
# Represent the graph as an adjacency list with weights
graph = {
    0: [(1, 3), (2, 6)],
    1: [(0, 3), (2, 2)],
    2: [(0, 6), (1, 2)]
}

# Run Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Print the results
for i in range(len(shortest_paths)):
    for j in range(len(shortest_paths[i])):
        print(f"Shortest distance from {i} to {j}: {shortest_paths[i][j]}")
