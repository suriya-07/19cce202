class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)
        self.queue.sort()

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

def dijkstra(graph, start):
    # Priority queue to store (distance, node) pairs
    _queue = Queue()
    _queue.push((0, start))
    visited = set()

    # Dictionary to store the minimum distance to each node
    distance = {node: float('infinity') for node in graph.nodes}
    distance[start] = 0

    while not _queue.is_empty():
        current_distance, current_node = _queue.pop()

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph.edges[current_node]:
            distance_to_neighbor = current_distance + weight

            if distance_to_neighbor < distance[neighbor]:
                distance[neighbor] = distance_to_neighbor
                _queue.push((distance_to_neighbor, neighbor))

    return distance

# Example usage:
g = Graph()

# Add nodes
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')

# Add edges with weights
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 7)

# Specify the starting node
start_node = 'A'

# Run Dijkstra's algorithm
shortest_distances = dijkstra(g, start_node)

# Print the results
for node, distance in shortest_distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")
