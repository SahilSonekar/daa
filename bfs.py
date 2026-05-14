from collections import deque

def bfs(graph, start):
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("\nBFS Sequence:- ")

    while queue:

        current = queue.popleft()
        print(current,end=" ")

        for i in graph[current]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

graph = {}
visited = set()
n = int(input("Enter the number of node:- "))

for i in range(n):

    node = input("Enter node:- ")
    neighbour = input(f"Enter neighbors of {node} separated by space:- ").split()
    graph[node] = neighbour

start = input("Enter the starting node:- ")

bfs(graph, start)

# ADDED PART FOR DISCONNECTED GRAPH
for node in graph:

    if node not in visited:

        bfs(graph, node, visited)