import heapq

def dijkstra(graph, start):

    distance = {}

    for node in graph:
        distance[node] = float('inf')

    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

                heapq.heappush(pq, (new_distance, neighbor))

    print("\nShortest Distances:")

    for node in distance:
        print(start, "to", node, "=", distance[node])


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")

    neighbors = int(input(f"Enter number of neighbors for {node}: "))

    graph[node] = []

    for j in range(neighbors):
        neighbor = input("Enter neighbor node: ")
        weight = int(input("Enter edge weight: "))

        graph[node].append((neighbor, weight))

start = input("Enter starting node: ")

dijkstra(graph, start)