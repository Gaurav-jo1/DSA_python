# Undirect Path
class Graph:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def edges_to_graph(self, edges):
        for edge in edges:
            if len(edge) < 2:
                self.graph[edge[0]] = []
                continue

            vertex1, vertex2 = edge

            # Adding vertex1 to vertex2's adjacency list
            if vertex1 in self.graph:
                self.graph[vertex1].append(vertex2)
            else:
                self.graph[vertex1] = [vertex2]

            # Adding vertex2 to vertex1's adjacency list
            if vertex2 in self.graph:
                self.graph[vertex2].append(vertex1)
            else:
                self.graph[vertex2] = [vertex1]

    def dfs(self, src, dst):
        self.visited.add(src)

        if src == dst:
            return True

        for neighbor in self.graph[src]:
            if neighbor not in self.visited:
                if self.dfs(neighbor, dst):
                    return True
        return False


# edges = [["i", "j"], ["k", "i"], ["m", "k"], ["k", "l"], ["o", "n"]]
edges = [
    ["b", "a"],
    ["c", "a"],
    ["b", "c"],
    ["q", "r"],
    ["q", "s"],
    ["q", "u"],
    ["q", "t"],
]
graph = Graph()
graph.edges_to_graph(edges)

print(graph.dfs("a", "b"))
