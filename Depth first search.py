def dfs(graph, starting_node):
   
    visited = set()  # Set to keep track of visited nodes

    def dfs_util(node):
        visited.add(node)
        print(node, end=' ')  # Print node as it's visited

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_util(neighbor)

    dfs_util(starting_node)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')  
