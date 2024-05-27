from collections import defaultdict, deque


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

def bfs_furthest_vertices(graph, start):
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        for neighbor, _ in graph[current_node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)

    max_distance = max(distances.values())
    furthest_vertices = [node for node, dist in distances.items() if dist == max_distance]
    return furthest_vertices, max_distance

furthest_vertices, furthest_distance = bfs_furthest_vertices(graph, S)

print("vertex dengan jarak terjauh dari S:", furthest_vertices)
print("Jarak", furthest_distance)