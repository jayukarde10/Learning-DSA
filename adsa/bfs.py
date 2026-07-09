from collections import deque

# BFS Algorithm
def bfs(graph, start, goal):
    visited = []
    queue = deque([start])

    visited.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("\nGoal Not Found!")

# State Space Graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

start = 'S'
goal = 'G'

print("BFS Traversal:")
bfs(graph, start, goal)