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

def dfs_exact_distance(graph, start, target_distance):
    stack = [(start, 0, [start])]

    while stack:
        current_node, current_distance, path = stack.pop()
        
        if current_distance == target_distance:
            return path
        
        if current_distance > target_distance:
            continue
        
        for neighbor, weight in graph[current_node]:
            if neighbor not in path:  # Ensure no revisits in the current path
                stack.append((neighbor, current_distance + weight, path + [neighbor]))
    return None

path_2024 = dfs_exact_distance(graph, S, 2024)

if path_2024:
    print("Vertex dengan jarak 2024 dari S : ", path_2024[-1])
    print("Path:", " -> ".join(map(str, path_2024)))
else:
    print("Tidak ada vertex dengan jarak 2024 dari S.")