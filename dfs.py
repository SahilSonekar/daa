def dfs(graph, node, visited):
    
    if node not in visited:
        print(node,end=" ")

        visited.add(node)

        for neigh in graph[node]:
            dfs(graph, neigh, visited)

graph = {}
visited = set()

n = int(input("Enter the number of nodes:- "))

for i in range(n):
    node = input("Enter node:- ")

    neigh = input(f"Enter the neighbour of {node} node seprated by spaces:- ").split()

    graph[node] = neigh

start = input("Enter the starting node:- ")

print("\nDFS Sequence:- ")
dfs(graph, start, visited)

# ADDED PART FOR DISCONNECTED GRAPH
for node in graph:

    if node not in visited:

        dfs(graph, node, visited)