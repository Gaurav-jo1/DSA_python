class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, edges):
        self.graph[vertex] = edges

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(vertex)
        print(vertex, end=" ")

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)


graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5])
graph.add_edge(3, [])
graph.add_edge(4, [])
graph.add_edge(5, [])

print("DFS starting from vertex 1:")
graph.dfs(1)
print(" ")
