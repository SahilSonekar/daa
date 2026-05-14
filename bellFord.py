def bellman_ford(graph, start):

    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    n = len(graph)

    for i in range(n - 1):

        for u in graph:

            for v, w in graph[u]:

                if distance[u] != float('inf') and distance[u] + w < distance[v]:

                    distance[v] = distance[u] + w

    negative_cycle = False

    for u in graph:

        for v, w in graph[u]:

            if distance[u] != float('inf') and distance[u] + w < distance[v]:

                negative_cycle = True
                break

    if negative_cycle:
        print("\nGraph contains negative weight cycle")

    else:
        print("\nShortest Distances:")

        for node in distance:
            print(start, "to", node, "=", distance[node])


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input("Enter node: ")

    graph[node] = []

    edges = int(input(f"Enter number of neighbors for {node}: "))

    for j in range(edges):

        neighbor = input("Enter neighbor node: ")

        weight = int(input("Enter edge weight: "))

        graph[node].append((neighbor, weight))

start = input("Enter starting node: ")

bellman_ford(graph, start)