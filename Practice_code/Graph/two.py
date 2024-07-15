class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_edge(self, vertex, edges):
        self.graph[vertex] = edges

    def bfs(self, start):
        visted = set()
        queue = [start]
        visted.add(start)

        while queue:
            current_index = queue.pop(0)
            print(current_index, end=" ")

            for neigbhour in self.graph[current_index]:
                if neigbhour not in visted:
                    queue.append(neigbhour)


graph = Graph()
graph.add_edge(1, [2, 3])
graph.add_edge(2, [4, 5])
graph.add_edge(3, [])
graph.add_edge(4, [])
graph.add_edge(5, [])

print("BFS starting from vertex 1:")
graph.bfs(1)
print("")
