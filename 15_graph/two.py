class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edges):
        self.graph[vertex] = edges

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example usage:
graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5])
graph.add_edge(3, [])
graph.add_edge(4, [])
graph.add_edge(5, [])

print("BFS starting from vertex 1:")
graph.bfs(1)
print("")