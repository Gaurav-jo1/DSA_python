def hasPath(graph, start, end):

    visted = set()

    def dfs(node):

        if node == end:
            return True

        visted.add(node)

        for neighbour in graph.get(node):
            if neighbour not in visted:
                if dfs(neighbour):
                    return True

        return False

    return dfs(start)


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

# Check if there is a path from 'A' to 'F'
result = hasPath(graph, "f", "k")
print(result)  # Output: True
