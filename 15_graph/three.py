def hasPath(graph, src, dst):
    visited = set()

    def dfs(node):
        if node == dst:
            return True

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        return False

    return dfs(src)


# Example usage:
# Define an adjacency list for a directed acyclic graph
graph = {
  "f": ['g', 'i'],
  "g": ['h'],
  "h": [],
  "i": ['g', 'k'],
  "j": ['i'],
  "k": []
}

# Check if there is a path from 'A' to 'F'
result = hasPath(graph, 'f', 'k')
print(result)  # Output: True
