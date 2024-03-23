def hasPath(graph, src, dst):
    visited = set()

    def dfs(node):
        if node == dst:
            return True

        visited.add(node)

        for neigbours in graph.get(node, []):
            if neigbours not in visited:
                if dfs(neigbours):
                    return True

        return False

    return dfs(src)

graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

# Check if there is a path from 'A' to 'F'
result = hasPath(graph, "f", "k")
print(result)  # Output: True
