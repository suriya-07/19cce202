def prim(graph):
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])
    minimum_spanning_tree = []
    priority_queue = [(weight, start_vertex, neighbor) for neighbor, weight in graph[start_vertex]]
    priority_queue.sort(key=lambda x: x[0])

    while priority_queue:
        weight, current_vertex, next_vertex = priority_queue.pop(0)

        if next_vertex not in visited:
            visited.add(next_vertex)
            minimum_spanning_tree.append((current_vertex, next_vertex, weight))

            for neighbor, weight in graph[next_vertex]:
                if neighbor not in visited:
                    priority_queue.append((weight, next_vertex, neighbor))
                    priority_queue.sort(key=lambda x: x[0])

    return minimum_spanning_tree


# Example usage:
# Represent the graph as an adjacency list with weights
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Run Prim's algorithm
minimum_spanning_tree = prim(graph)

# Print the results
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
