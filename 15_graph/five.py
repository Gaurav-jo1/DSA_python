def connectedComponentsCount(graph):
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited_nodes = set()
    components_count = 0

    for node in graph:
        if node not in visited_nodes:
            dfs(node, visited_nodes)
            components_count += 1

    return components_count

graph = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}

result = connectedComponentsCount(graph)
print(result)