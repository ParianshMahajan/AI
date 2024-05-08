def heuristic(graph, current_node, visited, start_node):
    unvisited = set(graph.keys()) - set(visited)  # Change visited to a set
    if len(unvisited) == 0:
        return graph[current_node][start_node]
    return min(graph[current_node].get(n, float('inf')) for n in unvisited)

def a_star(graph, start_node):
    path = []
    visited = []  # Change visited to a set
    total_cost = 0
    openlist = [(0, start_node)]
    while openlist:
        cost, current_node = min(openlist)
        openlist.remove((cost, current_node))
        if current_node in visited:
            continue
        path.append(current_node)
        visited.append(current_node)  # Append to visited
        if len(visited) == len(graph):
            total_cost += graph[current_node][start_node]
            path.append(start_node)
            return path, total_cost
        for neighbour, distance in graph[current_node].items():
            if neighbour not in visited:
                h = heuristic(graph, current_node, visited, start_node)  # Pass current_node to heuristic
                openlist.append((h + distance, neighbour))
        total_cost += cost
    return None, None

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}
start_node = 'A'
path, cost = a_star(graph, start_node)
print("Path:", path)
print("Total Cost:", cost)
