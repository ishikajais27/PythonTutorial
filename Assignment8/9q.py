graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# BFS
def bfs(start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    print()

# DFS
def dfs(start, visited):
    visited.append(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)

bfs(0)
print("DFS Traversal:", end=" ")
dfs(0, [])
print()
