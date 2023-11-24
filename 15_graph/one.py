# Depth First: Stack


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edges):
        self.graph[vertex] = edges

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5])
graph.add_edge(3, [])
graph.add_edge(4, [])
graph.add_edge(5, [])

print("DFS starting from vertex 1:")
graph.dfs(1)
print(" ")
