def prims_algorithm(graph):
   
    mst = []  # List to store MST edges
    visited = set()  # Set to keep track of visited nodes

    # Start with an arbitrary node
    start_node = next(iter(graph))
    visited.add(start_node)

    # Create a list to store potential edges for the MST (used as a priority queue)
    pq = [(0, None, start_node)]  # (weight, parent, node)

    while pq:
        # Manually find and remove the edge with minimum weight
        min_index = 0
        for i in range(1, len(pq)):
            if pq[i][0] < pq[min_index][0]:
                min_index = i
        weight, parent, node = pq.pop(min_index)

        if node not in visited:
            visited.add(node)
            mst.append((parent, node, weight))  # Add edge to MST

            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    pq.append((weight, node, neighbor))

    return mst
graph = {
    'A': {'B': 5, 'C': 7},
    'B': {'A': 5, 'D': 9, 'E': 3},
    'C': {'A': 7, 'F': 4},
    'D': {'B': 9, 'E': 2},
    'E': {'B': 3, 'D': 2, 'F': 6},
    'F': {'C': 4, 'E': 6}
}

mst = prims_algorithm(graph)
print(mst)  
