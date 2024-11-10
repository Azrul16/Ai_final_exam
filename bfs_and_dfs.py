from collections import deque
import time


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path + [current_node]

        if current_node not in visited:
            visited.add(current_node)
            queue.extend((neighbor, path + [current_node]) for neighbor in set(graph[current_node]) - visited)

    return []


def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [])]

    while stack:
        current_node, path = stack.pop()

        if current_node == goal:
            return path + [current_node]

        if current_node not in visited:
            visited.add(current_node)
            stack.extend((neighbor, path + [current_node]) for neighbor in set(graph[current_node]) - visited)

    return []


graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {},
    'D': {'F'},
    'E': {'H', 'G'},
    'F': {},
    'G': {'I', 'J'},
    'H': {'K'},
    'I': {'L'},
    'J': {'L'},
    'K': {},
    'L': {}
}

start_node = 'A'
goal_node = 'L'

start_time = time.time()
print("BFS Traversal:")
bfs_path = bfs(graph, start_node, goal_node)
print(f"BFS Result: {'Goal found' if bfs_path else 'Goal not found'}")
print(f"Traversal Path: {bfs_path}")
print("Runtime:", time.time() - start_time, "seconds")
print("Time complexity Status for BFS: Satisfy" if bfs_path else "Status: Not Satisfy")

start_time = time.time()
print("\nDFS Traversal:")
dfs_path = dfs(graph, start_node, goal_node)
print(f"DFS Result: {'Goal found' if dfs_path else 'Goal not found'}")
print(f"Traversal Path: {dfs_path}")
print("Runtime:", time.time() - start_time, "seconds")
print("Time complexity Status for DFS: Satisfy" if dfs_path else "Status: Not Satisfy")