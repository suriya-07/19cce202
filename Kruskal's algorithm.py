class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((vertex, neighbor, weight))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight in ascending order

    minimum_spanning_tree = []
    disjoint_set = DisjointSet(graph.keys())

    for edge in edges:
        vertex1, vertex2, weight = edge
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            disjoint_set.union(vertex1, vertex2)
            minimum_spanning_tree.append((vertex1, vertex2, weight))

    return minimum_spanning_tree


# Example usage:
# Represent the graph as an adjacency list with weights
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

# Run Kruskal's algorithm
minimum_spanning_tree = kruskal(graph)

# Print the results
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} - {edge[1]} : {edge[2]}")
