def bfs(graph, starting_node):
   
    visited = set()  # Set to keep track of visited nodes
    queue = []  # Use a list as a queue
    queue.append(starting_node)

    while queue:
        current_node = queue.pop(0)  # Remove from the front of the list
        visited.add(current_node)

        print(current_node, end=' ')  # Print node as it's visited

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  
