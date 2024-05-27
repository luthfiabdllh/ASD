import heapq
from collections import defaultdict


file_path = 'data.txt'

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    N, M = map(int, lines[0].split())
    edges = []
    for line in lines[1:M+1]:
        p1, p2, d = map(int, line.split())
        edges.append((p1, p2, d))
    S = int(lines[M+1].strip())
    return N, M, edges, S

N, M, edges, S = read_data(file_path)


graph = defaultdict(list)
for p1, p2, d in edges:
    graph[p1].append((p2, d))
    graph[p2].append((p1, d))


def dijkstra(graph, start):
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

distances = dijkstra(graph, S)
max_distance_vertex = max(distances, key=distances.get)
max_distance = distances[max_distance_vertex]

print("Vertex dengan jarak terpendek tertinggi dari S : ", max_distance_vertex)
print("Jarak tependek tertinggi : ", max_distance)